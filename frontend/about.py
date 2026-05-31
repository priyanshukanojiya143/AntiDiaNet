import streamlit as st
import streamlit.components.v1 as components


def about_page():

    # ── Global CSS injected via st.markdown (safe, no complex HTML) ──
    st.markdown("""
        <style>
        section[data-testid="stAppViewContainer"] > div,
        .stApp > div { background-color: #f5f7f5; }
        </style>
    """, unsafe_allow_html=True)

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap" rel="stylesheet"/>
    <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
        font-family: 'DM Sans', sans-serif;
        background: #f5f7f5;
        color: #1a1f2e;
        padding: 8px 16px 40px;
    }

    .ad-root { max-width: 1100px; margin: 0 auto; }

    /* ── Hero ── */
    .ad-hero {
        background: linear-gradient(135deg, #0b3528 0%, #145c44 50%, #1a7a5a 100%);
        border-radius: 20px;
        padding: 54px 64px 46px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .ad-hero::before {
        content: '';
        position: absolute;
        top: -70px; right: -70px;
        width: 340px; height: 340px;
        background: rgba(255,255,255,0.04);
        border-radius: 50%;
        pointer-events: none;
    }
    .ad-hero::after {
        content: '';
        position: absolute;
        bottom: -90px; left: 32%;
        width: 240px; height: 240px;
        background: rgba(255,255,255,0.03);
        border-radius: 50%;
        pointer-events: none;
    }
    .ad-hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,0.11);
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 100px;
        padding: 5px 16px 5px 10px;
        font-size: 11.5px;
        font-weight: 500;
        letter-spacing: 0.7px;
        color: #a8edcc;
        text-transform: uppercase;
        margin-bottom: 18px;
    }
    .dot {
        width: 7px; height: 7px;
        background: #4ade80;
        border-radius: 50%;
        display: inline-block;
        animation: pulse 2s ease-in-out infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50%       { opacity: 0.45; transform: scale(0.75); }
    }
    .ad-hero-title {
        font-family: 'DM Serif Display', serif;
        font-size: 46px;
        font-weight: 400;
        color: #fff;
        line-height: 1.12;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    .ad-hero-title em {
        font-style: italic;
        color: #7ce8b5;
    }
    .ad-hero-subtitle {
        font-size: 17px;
        font-weight: 300;
        color: rgba(255,255,255,0.65);
        margin-top: 2px;
        letter-spacing: 0.1px;
    }
    .ad-hero-desc {
        font-size: 15px;
        font-weight: 300;
        color: rgba(255,255,255,0.68);
        line-height: 1.7;
        max-width: 580px;
        margin-top: 16px;
    }

    /* ── Stats ── */
    .ad-stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-bottom: 28px;
    }
    .ad-stat {
        background: #ffffff;
        border: 1px solid #dde8e2;
        border-radius: 14px;
        padding: 20px 16px 16px;
        text-align: center;
    }
    .ad-stat-icon { font-size: 22px; display: block; margin-bottom: 8px; }
    .ad-stat-value {
        font-family: 'DM Serif Display', serif;
        font-size: 24px;
        color: #0b3528;
        line-height: 1;
        margin-bottom: 5px;
    }
    .ad-stat-label {
        font-size: 11.5px;
        font-weight: 500;
        color: #6b8c7a;
        letter-spacing: 0.3px;
        text-transform: uppercase;
    }

    /* ── Section heading ── */
    .ad-sh {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #1e6840;
        margin-bottom: 16px;
    }
    .ad-sh::after {
        content: '';
        flex: 1;
        height: 1px;
        background: #d4e5db;
    }

    /* ── Overview ── */
    .ad-overview {
        background: #ffffff;
        border: 1px solid #dde8e2;
        border-radius: 16px;
        padding: 28px 28px;
        margin-bottom: 28px;
        font-size: 14.5px;
        color: #3d4f47;
        line-height: 1.8;
    }
    .ad-overview strong { color: #1a1f2e; }

    /* ── Feature grid ── */
    .ad-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        margin-bottom: 28px;
    }
    .ad-card {
        background: #ffffff;
        border: 1px solid #dde8e2;
        border-radius: 16px;
        padding: 24px 22px 22px;
    }
    .ad-card-icon {
        width: 40px; height: 40px;
        background: #e6f4ed;
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 19px;
        margin-bottom: 12px;
    }
    .ad-card-title {
        font-size: 14.5px;
        font-weight: 600;
        color: #1a1f2e;
        margin-bottom: 12px;
        letter-spacing: -0.1px;
    }
    .ad-card ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .ad-card ul li {
        font-size: 13.5px;
        color: #4a5d54;
        line-height: 1.75;
        padding-left: 15px;
        position: relative;
    }
    .ad-card ul li::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: #2e7d55;
        font-size: 10px;
        top: 4px;
    }

    /* ── SHAP card ── */
    .ad-shap {
        background: linear-gradient(135deg, #eef8f2 0%, #e1f2e9 100%);
        border: 1px solid #bdd8c9;
        border-radius: 16px;
        padding: 28px 28px 24px;
        margin-bottom: 28px;
        display: grid;
        grid-template-columns: 1fr auto;
        gap: 28px;
        align-items: start;
    }
    .ad-shap-badge {
        display: inline-block;
        background: #1a6b40;
        color: #fff;
        font-size: 10.5px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .ad-shap-title {
        font-size: 17px;
        font-weight: 600;
        color: #0b3528;
        margin-bottom: 10px;
    }
    .ad-shap-body {
        font-size: 13.5px;
        color: #2d6648;
        line-height: 1.78;
    }
    .ad-shap-body strong { color: #0b3528; }
    .ad-pills {
        display: flex;
        flex-direction: column;
        gap: 8px;
        min-width: 185px;
    }
    .ad-pill {
        background: #fff;
        border: 1px solid #bdd8c9;
        border-radius: 100px;
        padding: 7px 14px;
        font-size: 12px;
        color: #0b4a2c;
        font-weight: 500;
        text-align: center;
        white-space: nowrap;
    }

    /* ── Disclaimer ── */
    .ad-disclaimer {
        background: #fffbf0;
        border: 1px solid #f0d98a;
        border-left: 4px solid #d4a000;
        border-radius: 12px;
        padding: 17px 22px;
        margin-bottom: 28px;
        font-size: 13.5px;
        color: #5a4500;
        line-height: 1.68;
    }
    .ad-disclaimer strong { color: #3d2e00; }

    /* ── Footer ── */
    .ad-footer {
        border-top: 1px solid #d4e5db;
        padding-top: 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 10px;
    }
    .ad-footer-copy { font-size: 12.5px; color: #8fa89a; }
    .ad-footer-tag {
        font-size: 11.5px;
        background: #e6f4ed;
        color: #1a6b40;
        font-weight: 600;
        padding: 4px 14px;
        border-radius: 100px;
    }

    @media (max-width: 780px) {
        .ad-stats { grid-template-columns: 1fr 1fr; }
        .ad-grid   { grid-template-columns: 1fr; }
        .ad-shap   { grid-template-columns: 1fr; }
        .ad-hero   { padding: 34px 24px 28px; }
        .ad-hero-title { font-size: 34px; }
        .ad-pills  { flex-direction: row; flex-wrap: wrap; }
    }
    </style>
    </head>
    <body>
    <div class="ad-root">

      <!-- HERO -->
      <div class="ad-hero">
        <div class="ad-hero-badge">
          <span class="dot"></span>
          In-Silico Drug Discovery Platform
        </div>
        <div class="ad-hero-title">Anti<em>Dia</em>Net</div>
        <div class="ad-hero-subtitle">AI-Powered Antidiabetic Activity Screening</div>
        <p class="ad-hero-desc">
          A computational platform integrating cheminformatics, machine learning, and
          explainable AI to accelerate early-stage natural product drug discovery —
          before the first experiment begins.
        </p>
      </div>

      <!-- STATS -->
      <div class="ad-stats">
        <div class="ad-stat">
          <span class="ad-stat-icon">🌿</span>
          <div class="ad-stat-value">Phyto</div>
          <div class="ad-stat-label">Phytochemical Focus</div>
        </div>
        <div class="ad-stat">
          <span class="ad-stat-icon">🌲</span>
          <div class="ad-stat-value">RF</div>
          <div class="ad-stat-label">Random Forest Model</div>
        </div>
        <div class="ad-stat">
          <span class="ad-stat-icon">⚡</span>
          <div class="ad-stat-value">Batch</div>
          <div class="ad-stat-label">High-Throughput Ready</div>
        </div>
        <div class="ad-stat">
          <span class="ad-stat-icon">🔬</span>
          <div class="ad-stat-value">SHAP</div>
          <div class="ad-stat-label">Explainable AI</div>
        </div>
      </div>

      <!-- OVERVIEW -->
      <div class="ad-sh">Overview</div>
      <div class="ad-overview">
        <strong>AntiDiaNet</strong> is an AI-powered web application developed for
        <strong>in-silico screening of antidiabetic activity</strong> in chemical compounds,
        with primary emphasis on <strong>plant-derived phytochemicals</strong>.
        The platform is designed to assist researchers in rapidly identifying promising
        antidiabetic candidates prior to experimental validation — accelerating
        early-stage natural product drug discovery. By reducing dependency on exhaustive
        laboratory screening, AntiDiaNet supports faster, cost-effective hypothesis
        generation for diabetes-related therapeutic research.
      </div>

      <!-- CAPABILITIES GRID -->
      <div class="ad-sh">Platform Capabilities</div>
      <div class="ad-grid">

        <div class="ad-card">
          <div class="ad-card-icon">🔍</div>
          <div class="ad-card-title">Core Capabilities</div>
          <ul>
            <li>Single compound prediction via SMILES notation</li>
            <li>Batch prediction for high-throughput compound screening</li>
            <li>Automatic SMILES retrieval from chemical names</li>
            <li>Binary classification — Active vs. Inactive</li>
            <li>Probability-based confidence scoring</li>
          </ul>
        </div>

        <div class="ad-card">
          <div class="ad-card-icon">⚗️</div>
          <div class="ad-card-title">Cheminformatics Methodology</div>
          <ul>
            <li>RDKit-based molecular descriptor generation</li>
            <li>MACCS keys and Morgan (ECFP) fingerprint encoding</li>
            <li>Random Forest feature selection for dimensionality reduction</li>
            <li>Robust imputation and feature standardization</li>
            <li>Cross-validation and independent test set evaluation</li>
          </ul>
        </div>

        <div class="ad-card">
          <div class="ad-card-icon">🤖</div>
          <div class="ad-card-title">Machine Learning Framework</div>
          <ul>
            <li>Optimized Random Forest classifier as final model</li>
            <li>Benchmarked against alternative ML architectures</li>
            <li>Evaluated on Accuracy, Precision, Recall, F1, ROC-AUC</li>
            <li>Strong generalization on held-out test data</li>
          </ul>
        </div>

        <div class="ad-card">
          <div class="ad-card-icon">🌾</div>
          <div class="ad-card-title">Research Scope</div>
          <ul>
            <li>Medicinal plants and agriculturally important crops</li>
            <li>Bioactive compounds from food systems (pulses, oilseeds)</li>
            <li>Nutraceutical and functional food development</li>
            <li>Natural-product-based therapeutic discovery</li>
          </ul>
        </div>

      </div>

      <!-- SHAP -->
      <div class="ad-sh">Explainable AI</div>
      <div class="ad-shap">
        <div>
          <span class="ad-shap-badge">SHAP Analysis</span>
          <div class="ad-shap-title">Interpretable, Biologically Grounded Predictions</div>
          <p class="ad-shap-body">
            AntiDiaNet integrates <strong>SHAP (SHapley Additive exPlanations)</strong>
            to improve interpretability and scientific transparency. Feature attribution
            analysis revealed that molecular surface area descriptors, electronic-state
            properties, lipophilicity-related descriptors, and structural fingerprint
            patterns are the primary drivers — supporting strong biological relevance
            of the underlying model.
          </p>
        </div>
        <div class="ad-pills">
          <div class="ad-pill">📐 Surface Area Descriptors</div>
          <div class="ad-pill">⚡ Electronic State Properties</div>
          <div class="ad-pill">💧 Lipophilicity Descriptors</div>
          <div class="ad-pill">🔩 Structural Fingerprints</div>
        </div>
      </div>

      <!-- DISCLAIMER -->
      <div class="ad-disclaimer">
        <strong>⚠️ Academic &amp; Research Use Only — </strong>
        AntiDiaNet is intended strictly for academic and research purposes.
        All predictions generated by this platform represent
        <strong>computational hypotheses</strong> and must be validated through
        biological experiments, pharmacological assays, or clinical investigation
        before any applied use. This tool does not replace laboratory validation,
        biological assays, or clinical decision-making.
      </div>

      <!-- FOOTER -->
      <div class="ad-footer">
        <span class="ad-footer-copy">AntiDiaNet · In-Silico Antidiabetic Screening Platform</span>
        <span class="ad-footer-tag">For Research Use Only</span>
      </div>

    </div>
    </body>
    </html>
    """

    components.html(html_content, height=1900, scrolling=False)


if __name__ == "__main__":
    about_page()