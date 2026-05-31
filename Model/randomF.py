import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.preprocessing import StandardScaler

# -------------------- CONFIG --------------------
TRAIN_PATH = "train_dataset.csv"
TEST_PATH = "test_dataset.csv"
SELECTED_FEATURES_PATH = "selected_features.pkl"
SCALER_OUT = "scaler_rf.pkl"
MODEL_OUT = "rf_model.pkl"
METRICS_OUT = "rf_all_metrics.xlsx"

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# -------------------- HELPERS --------------------
def compute_metrics(y_true, y_pred, y_prob):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "auc": roc_auc_score(y_true, y_prob),
        "f1": f1_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "conf_matrix": confusion_matrix(y_true, y_pred).tolist()
    }

# -------------------- LOAD DATA --------------------
print("\n📥 Loading datasets...")
df_train = pd.read_csv(TRAIN_PATH)
df_test = pd.read_csv(TEST_PATH)
selected_features = joblib.load(SELECTED_FEATURES_PATH)

# Drop metadata columns if present
metadata_cols = ["SMILES", "Name", "Chemical Name"]
df_train = df_train.drop(columns=[col for col in metadata_cols if col in df_train.columns], errors="ignore")
df_test = df_test.drop(columns=[col for col in metadata_cols if col in df_test.columns], errors="ignore")

X_train = df_train[selected_features]
y_train = df_train["Label"]
X_test = df_test[selected_features]
y_test = df_test["Label"]

# Clean and scale
medians = X_train.median()
X_train = X_train.replace([np.inf, -np.inf], np.nan).fillna(medians)
X_test = X_test.replace([np.inf, -np.inf], np.nan).fillna(medians)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
joblib.dump(scaler, SCALER_OUT)

# -------------------- 5-FOLD CV --------------------
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
fold_results = []

print("\n🔁 Performing 5-fold cross-validation...")
for fold, (train_idx, val_idx) in enumerate(skf.split(X_train_scaled, y_train)):
    X_tr, X_val = X_train_scaled[train_idx], X_train_scaled[val_idx]
    y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]

    clf = RandomForestClassifier(random_state=RANDOM_STATE, n_jobs=-1)
    clf.fit(X_tr, y_tr)
    y_val_pred = clf.predict(X_val)
    y_val_prob = clf.predict_proba(X_val)[:, 1]
    fold_results.append(pd.Series(compute_metrics(y_val, y_val_pred, y_val_prob), name=f"Fold_{fold+1}"))

# -------------------- FINAL TRAINING --------------------
print("\n🚀 Training final model on full training data...")
final_model = RandomForestClassifier(random_state=RANDOM_STATE, n_jobs=-1)
final_model.fit(X_train_scaled, y_train)
joblib.dump(final_model, MODEL_OUT)

# Evaluate on train
train_pred = final_model.predict(X_train_scaled)
train_prob = final_model.predict_proba(X_train_scaled)[:, 1]
train_metrics = pd.Series(compute_metrics(y_train, train_pred, train_prob), name="Train")

# Evaluate on test
test_pred = final_model.predict(X_test_scaled)
test_prob = final_model.predict_proba(X_test_scaled)[:, 1]
test_metrics = pd.Series(compute_metrics(y_test, test_pred, test_prob), name="Test")

# -------------------- SAVE RESULTS --------------------
print("\n💾 Saving all metrics to Excel...")
result_df = pd.concat(fold_results + [train_metrics, test_metrics], axis=1)
result_df.to_excel(METRICS_OUT)

print("\n✅ Random Forest Training Complete!")
print("📁 Metrics saved to:", METRICS_OUT)
print("💾 Model saved to:", MODEL_OUT)
print("💾 Scaler saved to:", SCALER_OUT)