# anti_dianet_backend.py
"""
AntiDiaNet backend — Clean, fixed, production-ready.
Features:
 - Name -> SMILES: PubChem (PUG REST) -> OPSIN -> ChEBI (fallback)
 - SMILES validation & canonicalization via RDKit
 - Deterministic RDKit descriptors, Morgan (ECFP) fingerprints, MACCS keys
 - Align to selected_features.pkl, median impute, scale, predict
 - Exposes: predict_single(input_str), predict_batch(list_of_inputs), extract_features_single(smiles)
"""

import os
import re
import time
import joblib
import requests
import numpy as np
import pandas as pd
from typing import List, Tuple, Optional
from rdkit import Chem, DataStructs
from rdkit.Chem import Descriptors, AllChem, MACCSkeys
from rdkit.ML.Descriptors import MoleculeDescriptors

# ---------------------- CONFIG (edit these paths to match your environment) ----------------------
MODEL_PATH = r"D:\Research\AntiDiaNET\Model\rf_model.pkl"
SCALER_PATH = r"D:\Research\AntiDiaNET\Model\scaler_rf.pkl"
SELECTED_FEATURES_PKL = r"D:\Research\AntiDiaNET\Model\selected_features.pkl"
MEDIANS_PKL = r"D:\Research\AntiDiaNET\Model\feature_medians.pkl"
REQUEST_TIMEOUT = 8            # network timeout seconds
PAUSE_BETWEEN_LOOKUPS = 0.12   # polite pause between external lookups
MAX_NAME_LEN_FOR_URL = 250

# fingerprint settings (must match training)
MORGAN_BITS = 1024
MORGAN_RADIUS = 2
MACCS_RAW = 167   # rdkit returns 167 bits; we drop index 0 -> 166 used

# ---------------------- ENSURE ARTIFACTS EXIST & LOAD ----------------------
_required = {
    "model": MODEL_PATH,
    "scaler": SCALER_PATH,
    "selected_features": SELECTED_FEATURES_PKL,
    "medians": MEDIANS_PKL
}
for name, path in _required.items():
    if not os.path.exists(path):
        raise FileNotFoundError(f"Required artifact '{name}' not found at: {path}")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
selected_features = joblib.load(SELECTED_FEATURES_PKL)
# ensure lower-case feature names to match alignment logic
selected_features = [c.lower() for c in selected_features]

medians = joblib.load(MEDIANS_PKL)
# normalize medians keys to lower-case
medians = {k.lower(): v for k, v in medians.items()}

# ---------------------- RDKit descriptor setup ----------------------
RD_DESC_LIST = [name for name, _ in Descriptors._descList]   # exact RDKit order
calculator = MoleculeDescriptors.MolecularDescriptorCalculator(RD_DESC_LIST)

FP_COLS = [f"fp_{i}" for i in range(MORGAN_BITS)]
MACCS_COLS = [f"maccs_{i}" for i in range(MACCS_RAW - 1)]   # drop index 0

ALL_EXTRACTED_FEATURES = [c.lower() for c in RD_DESC_LIST] + FP_COLS + MACCS_COLS

# ---------------------- Utilities ----------------------
def _canonicalize_smiles(smi: str) -> Optional[str]:
    """Return kekulized + canonical SMILES or None if invalid."""
    try:
        if smi is None:
            return None
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            return None
        Chem.Kekulize(mol, clearAromaticFlags=True)  # 🔧 NEW: ensure kekulization
        return Chem.MolToSmiles(mol, canonical=True, kekuleSmiles=True)
    except Exception:
        return None


def _safe_get(url: str, **kwargs) -> Optional[requests.Response]:
    """Safe requests.get wrapper."""
    try:
        return requests.get(url, timeout=REQUEST_TIMEOUT, **kwargs)
    except Exception:
        return None

def _quote_name_for_url(name: str) -> str:
    """Prepare a safe, limited-length query string for URLs."""
    s = str(name).strip()
    if len(s) > MAX_NAME_LEN_FOR_URL:
        s = s[:MAX_NAME_LEN_FOR_URL]
    return requests.utils.requote_uri(s)

# ---------------------- Name -> SMILES resolvers ----------------------
def _get_smiles_pubchem(name: str) -> Optional[str]:
    """PubChem PUG REST lookup for canonical SMILES (fast & primary)."""
    if not name:
        return None
    q = _quote_name_for_url(name)
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{q}/property/CanonicalSMILES/TXT"
    r = _safe_get(url)
    if r and r.status_code == 200:
        smi = r.text.strip()
        if smi and Chem.MolFromSmiles(smi):
            return smi
    return None

def _get_smiles_opsin(name: str) -> Optional[str]:
    """OPSIN structural name -> SMILES (good for IUPAC/systematic names)."""
    if not name:
        return None
    q = _quote_name_for_url(name)
    url = f"https://opsin.ch.cam.ac.uk/opsin/{q}.json"
    r = _safe_get(url)
    if r and r.status_code == 200:
        try:
            data = r.json()
            smi = data.get("smiles")
            if smi and Chem.MolFromSmiles(smi):
                return smi
        except Exception:
            return None
    return None

def _get_smiles_chebi(name: str) -> Optional[str]:
    """
    Best-effort ChEBI fallback:
    - Search page to find ChEBI id, then fetch detail REST to extract <smiles>.
    Note: EBI pages are scraped as fallback only.
    """
    if not name:
        return None
    q = _quote_name_for_url(name)
    search_url = f"https://www.ebi.ac.uk/chebi/searchId.do?searchString={q}"
    r = _safe_get(search_url)
    if not r:
        return None
    # find first ChEBI id (case-insensitive)
    m = re.search(r"ChEBI:(\d+)", r.text, re.IGNORECASE)
    if not m:
        return None
    chebi_id = m.group(1)
    detail_url = f"https://www.ebi.ac.uk/chebi/ws/rest/chebiId/CHEBI:{chebi_id}"
    r2 = _safe_get(detail_url)
    if not r2:
        return None
    m2 = re.search(r"<smiles>(.*?)</smiles>", r2.text, flags=re.IGNORECASE)
    if m2:
        smi = m2.group(1).strip()
        if smi and Chem.MolFromSmiles(smi):
            return smi
    return None

def resolve_smiles(input_str: str, pause: float = PAUSE_BETWEEN_LOOKUPS) -> Optional[str]:
    """
    Resolve an input that may be either a SMILES or a compound name.
    Order of attempts: if valid SMILES -> return canonical SMILES
                       PubChem -> OPSIN -> ChEBI
    Returns canonical SMILES string or None.
    """
    if input_str is None:
        return None
    s = str(input_str).strip()
    if s == "":
        return None

    # If it already parses as SMILES -> canonicalize and return
    if Chem.MolFromSmiles(s):
        return _canonicalize_smiles(s)

    # PubChem (primary)
    smi = _get_smiles_pubchem(s)
    if smi:
        return _canonicalize_smiles(smi)
    time.sleep(pause)

    # OPSIN (good for IUPAC/systematic names)
    smi = _get_smiles_opsin(s)
    if smi:
        return _canonicalize_smiles(smi)
    time.sleep(pause)

    # ChEBI fallback
    smi = _get_smiles_chebi(s)
    if smi:
        return _canonicalize_smiles(smi)

    return None

# ---------------------- Feature extraction ----------------------
def extract_rdkit_descriptors(smi: str):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return [np.nan] * len(RD_DESC_LIST)
    return calculator.CalcDescriptors(mol)

def extract_morgan_fp(smi: str, radius: int = MORGAN_RADIUS, nBits: int = MORGAN_BITS):
    arr = np.zeros((nBits,), dtype=int)
    mol = Chem.MolFromSmiles(smi)
    if mol:
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits)
        DataStructs.ConvertToNumpyArray(fp, arr)
    return arr

def extract_maccs_keys(smi: str):
    arr_full = np.zeros((MACCS_RAW,), dtype=int)
    mol = Chem.MolFromSmiles(smi)
    if mol:
        fp = MACCSkeys.GenMACCSKeys(mol)
        DataStructs.ConvertToNumpyArray(fp, arr_full)
    # drop first index to match training
    return arr_full[1:]

def extract_features_single(smi: str) -> pd.DataFrame:
    """
    Given a SMILES string (can be canonical or not), return 1-row DataFrame
    with columns ordered exactly as ALL_EXTRACTED_FEATURES (lower-case).
    """
    if smi is None:
        row = [np.nan] * len(ALL_EXTRACTED_FEATURES)
    else:
        smi_can = _canonicalize_smiles(smi)
        if smi_can is None:
            row = [np.nan] * len(ALL_EXTRACTED_FEATURES)
        else:
            rd = extract_rdkit_descriptors(smi_can)
            fp = extract_morgan_fp(smi_can)
            maccs = extract_maccs_keys(smi_can)
            row = np.concatenate([rd, fp, maccs])
    df = pd.DataFrame([row], columns=ALL_EXTRACTED_FEATURES)
    # force numeric types
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def extract_features_batch(smi_list: List[Optional[str]]) -> pd.DataFrame:
    """Extract features for a list of SMILES (some may be None)."""
    rows = []
    for smi in smi_list:
        if smi:
            smi_can = _canonicalize_smiles(smi)
            if smi_can:
                rd = extract_rdkit_descriptors(smi_can)
                fp = extract_morgan_fp(smi_can)
                maccs = extract_maccs_keys(smi_can)
                rows.append(np.concatenate([rd, fp, maccs]))
                continue
        rows.append([np.nan] * len(ALL_EXTRACTED_FEATURES))
    df = pd.DataFrame(rows, columns=ALL_EXTRACTED_FEATURES)
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

# ---------------------- Align to training ----------------------
def align_to_training(df: pd.DataFrame) -> pd.DataFrame:
    """
    Align extracted features (columns lower-case) to the exact selected_features order.
    Fill missing columns with medians and ensure numeric dtype.
    """
    df = df.copy()
    df.columns = [c.lower() for c in df.columns]

    # keep numeric only
    df = df.select_dtypes(include=[np.number])

    aligned = pd.DataFrame(index=df.index)

    for feat in selected_features:
        if feat in df.columns:
            aligned[feat] = df[feat]
        else:
            aligned[feat] = medians.get(feat, 0.0)

    # fill NaN/infs with medians
    for col in aligned.columns:
        aligned[col] = aligned[col].replace([np.inf, -np.inf], np.nan).fillna(medians.get(col, 0.0))

    # enforce order
    aligned = aligned[selected_features]
    return aligned

# ---------------------- Prediction helpers ----------------------
def predict_from_aligned_df(aligned_df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """Input: aligned dataframe (features in correct order). Output: preds (0/1), probs (float)."""
    X = scaler.transform(aligned_df.values)
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X)[:, 1]
    else:
        probs = model.predict(X).astype(float)
    preds = (probs >= 0.5).astype(int)
    return preds, probs

# ---------------------- Public API ----------------------
def predict_single(input_str: str) -> Tuple[Optional[int], Optional[float], Optional[str]]:
    """
    Accepts: a SMILES string or compound name.
    Returns: (label:int or None, probability:float or None, resolved_smiles or None)
    """
    if input_str is None:
        return None, None, None

    smi = resolve_smiles(input_str)
    if not smi:
        return None, None, None

    feats = extract_features_single(smi)
    aligned = align_to_training(feats)
    preds, probs = predict_from_aligned_df(aligned)
    return int(preds[0]), float(probs[0]), smi

def predict_batch(inputs: List[str]) -> Tuple[pd.DataFrame, List[dict]]:
    """
    Accepts: list of inputs (SMILES or names)
    Returns: (DataFrame with columns Input, Resolved_SMILES, Prediction, Probability, failures list)
    """
    resolved = []
    failures = []

    # Resolve each input exactly once (avoid duplicate lookups)
    for x in inputs:
        smi = resolve_smiles(x)
        if smi:
            resolved.append(smi)
        else:
            resolved.append(None)
            failures.append({"input": x, "error": "SMILES not found"})

    feats_df = extract_features_batch(resolved)
    aligned_df = align_to_training(feats_df)
    preds, probs = predict_from_aligned_df(aligned_df)

    out = pd.DataFrame({
        "Input": inputs,
        "Resolved_SMILES": [r if r is not None else "" for r in resolved],
        "Prediction": preds,
        "Probability": probs
    })

    return out, failures

# ---------------------- CLI quick test ----------------------
if __name__ == "__main__":
    examples = ["quercetin", "CC(=O)OC1=CC=CC=C1C(=O)O", "glucose", "C1=CC=CC=C1"]
    df_res, fails = predict_batch(examples)
    print(df_res)
    print("failures:", fails)
