import streamlit as st
import pandas as pd
import plotly.express as px
import backend


def prediction_page():

    # ── Inject CSS to theme all Streamlit native widgets ──
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif !important;
    }

    /* ── Hero banner ── */
    .pred-hero {
        background: linear-gradient(135deg, #0b3528 0%, #145c44 50%, #1a7a5a 100%);
        border-radius: 20px;
        padding: 44px 56px 38px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .pred-hero::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 300px; height: 300px;
        background: rgba(255,255,255,0.04);
        border-radius: 50%;
        pointer-events: none;
    }
    .pred-hero-badge {
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
        margin-bottom: 16px;
    }
    .pred-dot {
        width: 7px; height: 7px;
        background: #4ade80;
        border-radius: 50%;
        display: inline-block;
        animation: ppulse 2s ease-in-out infinite;
    }
    @keyframes ppulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50%       { opacity: 0.45; transform: scale(0.75); }
    }
    .pred-hero-title {
        font-family: 'DM Serif Display', serif;
        font-size: 42px;
        font-weight: 400;
        color: #fff;
        line-height: 1.12;
        letter-spacing: -0.5px;
        margin-bottom: 4px;
    }
    .pred-hero-title em { font-style: italic; color: #7ce8b5; }
    .pred-hero-sub {
        font-size: 16px;
        font-weight: 300;
        color: rgba(255,255,255,0.65);
    }
    .pred-hero-desc {
        font-size: 14.5px;
        font-weight: 300;
        color: rgba(255,255,255,0.65);
        line-height: 1.7;
        max-width: 560px;
        margin-top: 12px;
    }

    /* ── Section heading — same as about/contact ── */
    .pred-sh {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #1e6840;
        margin-bottom: 4px;
        margin-top: 4px;
    }
    .pred-sh::after {
        content: '';
        flex: 1;
        height: 1px;
        background: #d4e5db;
    }

    /* ── Result cards ── */
    .pred-result-wrap {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 14px;
        margin-top: 16px;
    }
    .pred-result-card {
        border-radius: 14px;
        padding: 18px 20px;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    .pred-result-card.active {
        background: #e6f4ed;
        border: 1px solid #b8dcc9;
    }
    .pred-result-card.inactive {
        background: #fdecea;
        border: 1px solid #f5b8b4;
    }
    .pred-result-card.info {
        background: #eef5ff;
        border: 1px solid #b8ceee;
    }
    .pred-result-card.neutral {
        background: #f5f7f5;
        border: 1px solid #dde8e2;
    }
    .pred-result-label {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: #6b8c7a;
        margin-bottom: 2px;
    }
    .pred-result-value {
        font-family: 'DM Serif Display', serif;
        font-size: 22px;
        font-weight: 400;
        color: #0b3528;
    }
    .pred-result-value.active  { color: #1a6b40; }
    .pred-result-value.inactive { color: #b91c1c; }
    .pred-result-value.info    { color: #1848a0; }
    .pred-smiles-card {
        background: #f5f7f5;
        border: 1px solid #dde8e2;
        border-radius: 12px;
        padding: 12px 16px;
        font-size: 12.5px;
        color: #3d6650;
        font-family: monospace;
        word-break: break-all;
        margin-top: 14px;
    }
    .pred-smiles-label {
        font-size: 10.5px;
        font-weight: 600;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        color: #8fa89a;
        margin-bottom: 4px;
    }

    /* ── Streamlit tab bar ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: #f0f5f2;
        padding: 5px 6px;
        border-radius: 12px;
        border-bottom: none !important;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 9px !important;
        padding: 7px 22px !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
        color: #4a6858 !important;
        background: transparent !important;
        border: none !important;
        transition: all 0.15s ease;
    }
    .stTabs [aria-selected="true"] {
        background: #ffffff !important;
        color: #0b3528 !important;
        font-weight: 600 !important;
        box-shadow: 0 1px 6px rgba(0,0,0,0.09) !important;
    }
    .stTabs [data-baseweb="tab-highlight"] { display: none !important; }
    .stTabs [data-baseweb="tab-border"]    { display: none !important; }

    /* ── Inputs ── */
    .stTextInput > div > div > input {
        border: 1.5px solid #ccddd5 !important;
        border-radius: 10px !important;
        font-size: 14px !important;
        padding: 10px 14px !important;
        background: #ffffff !important;
        transition: border-color 0.15s;
    }
    .stTextInput > div > div > input:focus {
        border-color: #1a7a5a !important;
        box-shadow: 0 0 0 3px rgba(26,122,90,0.1) !important;
    }

    /* ── Primary buttons ── */
    .stButton > button[kind="primary"],
    .stButton > button:not([kind]) {
        background: linear-gradient(135deg, #145c44, #1a7a5a) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 13.5px !important;
        font-weight: 600 !important;
        padding: 9px 22px !important;
        letter-spacing: 0.2px;
        transition: opacity 0.15s ease, transform 0.1s ease;
    }
    .stButton > button:hover {
        opacity: 0.9 !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ── Secondary / "Use Example" button ── */
    div[data-testid="column"]:last-child .stButton > button {
        background: #e6f4ed !important;
        color: #1a6b40 !important;
        border: 1.5px solid #bdd8c9 !important;
        border-radius: 10px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }
    div[data-testid="column"]:last-child .stButton > button:hover {
        background: #d4ecdf !important;
    }

    /* ── File uploader ── */
    [data-testid="stFileUploader"] {
        border: 2px dashed #bdd8c9 !important;
        border-radius: 14px !important;
        background: #f0f8f4 !important;
        padding: 8px;
    }

    /* ── Dataframe ── */
    [data-testid="stDataFrame"] {
        border: 1px solid #dde8e2 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }

    /* ── Plotly chart container ── */
    [data-testid="stPlotlyChart"] {
        border: 1px solid #dde8e2;
        border-radius: 14px;
        overflow: hidden;
        padding: 4px;
        background: #ffffff;
    }

    /* ── Download button ── */
    [data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #145c44, #1a7a5a) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 13.5px !important;
        font-weight: 600 !important;
        padding: 9px 22px !important;
        margin-top: 6px;
        transition: opacity 0.15s ease, transform 0.1s ease;
    }
    [data-testid="stDownloadButton"] > button:hover {
        opacity: 0.9 !important;
        transform: translateY(-1px) !important;
    }

    /* ── Hide default st.success / st.info boxes → replaced by custom cards ── */
    </style>
    """, unsafe_allow_html=True)

    # ── Hero Banner ──
    st.markdown("""
    <div class="pred-hero">
      <div class="pred-hero-badge">
        <span class="pred-dot"></span>
        Antidiabetic Activity Prediction
      </div>
      <div class="pred-hero-title">Pre<em>dict</em>ion Panel</div>
      <div class="pred-hero-sub">AI-Powered Phytochemical Screening</div>
      <p class="pred-hero-desc">
        Submit a SMILES string, a compound name, or a batch CSV to instantly screen
        for antidiabetic activity using our Random Forest model.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Section heading ──
    st.markdown('<div class="pred-sh">Choose Prediction Mode</div>', unsafe_allow_html=True)

    # ── Example data ──
    SMI_EXAMPLES = {
        "Aspirin":   "CC(=O)OC1=CC=CC=C1C(=O)O",
        "Quercetin": "O=C1C(=C(O)c2cc(O)cc(O)c21)c1ccc(O)c(O)c1",
        "Berberine": "COc1ccc2CC3=[N+](Cc4cc5c(cc4-3)OCO5)C=Cc2c1OC",
    }
    NAME_EXAMPLES = ["Quercetin", "Curcumin", "Resveratrol"]

    # ── Init buffer keys (never collide with widget keys) ──
    if "smi_val" not in st.session_state:
        st.session_state.smi_val = ""
    if "name_val" not in st.session_state:
        st.session_state.name_val = ""

    # ── Tabs ──
    tab1, tab2, tab3 = st.tabs(["🔬 Single — SMILES", "🧬 Single — Name", "📁 Batch CSV"])

    # ────────────────────────────────────────────────
    with tab1:
        st.markdown("##### Enter a SMILES string to predict antidiabetic activity")

        col1, col2 = st.columns([4, 1])
        with col2:
            st.markdown("<div style='margin-top:28px'></div>", unsafe_allow_html=True)
            chosen_smi = st.selectbox("Example", ["— Select Example —"] + list(SMI_EXAMPLES.keys()),
                                      key="dd_smi", label_visibility="collapsed")
            if chosen_smi != "— Select Example —":
                st.session_state.smi_val = SMI_EXAMPLES[chosen_smi]
        with col1:
            smi_typed = st.text_input("SMILES notation",
                                      value=st.session_state.smi_val,
                                      placeholder="e.g. CC(=O)OC1=CC=CC=C1C(=O)O")
            st.session_state.smi_val = smi_typed
        if st.button("Run Prediction", key="pred_smi"):
            with st.spinner("Analysing compound…"):
                label, prob, _ = backend.predict_single(st.session_state.smi_val)

            if prob is None or label is None:
                st.markdown("""
                <div class="pred-result-card inactive" style="margin-top:16px;padding:18px 20px;border-radius:14px;">
                  <div class="pred-result-label">Resolution Failed</div>
                  <div class="pred-result-value inactive" style="font-size:15px;">
                    ⚠️ Could not process this SMILES. Please check the structure and try again.
                  </div>
                </div>""", unsafe_allow_html=True)
            else:
                result_cls   = "active" if str(label).strip().lower() in ["1", "active"] else "inactive"
                result_label = "Active 🟢" if result_cls == "active" else "Inactive 🔴"
                conf_pct     = f"{float(prob)*100:.2f}%"

                st.markdown(f"""
                <div class="pred-result-wrap">
                  <div class="pred-result-card {result_cls}">
                    <div class="pred-result-label">Prediction</div>
                    <div class="pred-result-value {result_cls}">{result_label}</div>
                  </div>
                  <div class="pred-result-card neutral">
                    <div class="pred-result-label">Confidence Score</div>
                    <div class="pred-result-value">{conf_pct}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

    # ────────────────────────────────────────────────
    with tab2:
        st.markdown("##### Enter a compound name — SMILES will be resolved automatically")

        col1, col2 = st.columns([4, 1])
        with col2:
            st.markdown("<div style='margin-top:28px'></div>", unsafe_allow_html=True)
            chosen_name = st.selectbox("Example", ["— Select Example —"] + NAME_EXAMPLES,
                                       key="dd_name", label_visibility="collapsed")
            if chosen_name != "— Select Example —":
                st.session_state.name_val = chosen_name
        with col1:
            name_typed = st.text_input("Compound name",
                                       value=st.session_state.name_val,
                                       placeholder="e.g. Quercetin, Berberine, Curcumin")
            st.session_state.name_val = name_typed
        if st.button("Run Prediction", key="pred_name"):
            with st.spinner("Resolving name & analysing compound…"):
                label, prob, resolved = backend.predict_single(st.session_state.name_val)

            if prob is None or label is None:
                st.markdown(f"""
                <div class="pred-result-card inactive" style="margin-top:16px;padding:18px 20px;border-radius:14px;">
                  <div class="pred-result-label">Resolution Failed</div>
                  <div class="pred-result-value inactive" style="font-size:15px;">
                    ⚠️ Could not resolve <b>"{st.session_state.name_val}"</b> to a valid SMILES.
                    Try a more specific name, an IUPAC name, or paste the SMILES directly in Tab 1.
                  </div>
                </div>""", unsafe_allow_html=True)
            else:
                result_cls   = "active" if str(label).strip().lower() in ["1", "active"] else "inactive"
                result_label = "Active 🟢" if result_cls == "active" else "Inactive 🔴"
                conf_pct     = f"{float(prob)*100:.2f}%"

                st.markdown(f"""
                <div class="pred-result-wrap">
                  <div class="pred-result-card {result_cls}">
                    <div class="pred-result-label">Prediction</div>
                    <div class="pred-result-value {result_cls}">{result_label}</div>
                  </div>
                  <div class="pred-result-card neutral">
                    <div class="pred-result-label">Confidence Score</div>
                    <div class="pred-result-value">{conf_pct}</div>
                  </div>
                </div>
                <div class="pred-smiles-card">
                  <div class="pred-smiles-label">Resolved SMILES</div>
                  {resolved}
                </div>
                """, unsafe_allow_html=True)

    # ────────────────────────────────────────────────
    with tab3:
        st.markdown("##### Upload a CSV file — first column should contain SMILES strings")

        upload = st.file_uploader("Drop your CSV here", type=["csv"])
        if upload:
            df = pd.read_csv(upload)

            st.markdown('<div class="pred-sh" style="margin-top:16px">Preview — First 5 Rows</div>',
                        unsafe_allow_html=True)
            st.dataframe(df.head(), use_container_width=True)

            if st.button("Run Batch Prediction", key="pred_batch"):
                with st.spinner("Running batch prediction…"):
                    results, _ = backend.predict_batch(
                        df.iloc[:, 0].astype(str).tolist()
                    )

                st.markdown('<div class="pred-sh" style="margin-top:20px">Results</div>',
                            unsafe_allow_html=True)
                st.dataframe(results, use_container_width=True)

                # ── Download Button ──
                csv_data = results.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="⬇️ Download Results as CSV",
                    data=csv_data,
                    file_name="antidianet_batch_results.csv",
                    mime="text/csv",
                    key="download_results",
                )

                active_n   = int((results["Prediction"] == 1).sum())
                inactive_n = int((results["Prediction"] == 0).sum())
                total      = active_n + inactive_n

                # Summary cards
                st.markdown(f"""
                <div class="pred-result-wrap" style="margin-top:16px; margin-bottom:16px">
                  <div class="pred-result-card active">
                    <div class="pred-result-label">Active Compounds</div>
                    <div class="pred-result-value active">{active_n} &nbsp;<span style="font-size:15px;color:#4a8a6a">/ {total}</span></div>
                  </div>
                  <div class="pred-result-card inactive">
                    <div class="pred-result-label">Inactive Compounds</div>
                    <div class="pred-result-value inactive">{inactive_n} &nbsp;<span style="font-size:15px;color:#b06060">/ {total}</span></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown('<div class="pred-sh">Prediction Distribution</div>',
                            unsafe_allow_html=True)

                fig = px.pie(
                    names=["Active", "Inactive"],
                    values=[active_n, inactive_n],
                    hole=0.45,
                    color=["Active", "Inactive"],
                    color_discrete_map={"Active": "#1a7a5a", "Inactive": "#e05252"},
                )
                fig.update_traces(
                    textfont_size=14,
                    marker=dict(line=dict(color="#ffffff", width=2))
                )
                fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_family="DM Sans",
                    title=None,
                    legend=dict(font=dict(size=13)),
                    margin=dict(t=20, b=20, l=20, r=20),
                )
                st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    prediction_page()