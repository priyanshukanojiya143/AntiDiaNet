import streamlit as st
import os
from PIL import Image


def home_page():

    # ── CSS ──
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif !important;
    }

    /* ── Hero ── */
    .home-hero {
        background: linear-gradient(135deg, #0b3528 0%, #145c44 50%, #1a7a5a 100%);
        border-radius: 20px;
        padding: 64px 64px 54px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
        text-align: center;
    }
    .home-hero::before {
        content: '';
        position: absolute;
        top: -80px; right: -80px;
        width: 360px; height: 360px;
        background: rgba(255,255,255,0.04);
        border-radius: 50%;
        pointer-events: none;
    }
    .home-hero::after {
        content: '';
        position: absolute;
        bottom: -100px; left: 20%;
        width: 280px; height: 280px;
        background: rgba(255,255,255,0.03);
        border-radius: 50%;
        pointer-events: none;
    }
    .home-hero-badge {
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
        margin-bottom: 20px;
    }
    .home-dot {
        width: 7px; height: 7px;
        background: #4ade80;
        border-radius: 50%;
        display: inline-block;
        animation: hpulse 2s ease-in-out infinite;
    }
    @keyframes hpulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50%       { opacity: 0.45; transform: scale(0.75); }
    }
    .home-hero-title {
        font-family: 'DM Serif Display', serif;
        font-size: 48px;
        font-weight: 400;
        color: #ffffff;
        line-height: 1.15;
        letter-spacing: -0.5px;
        margin-bottom: 16px;
        position: relative;
        z-index: 1;
    }
    .home-hero-title em {
        font-style: italic;
        color: #7ce8b5;
    }
    .home-hero-desc {
        font-size: 17px;
        font-weight: 300;
        color: rgba(255,255,255,0.68);
        line-height: 1.7;
        max-width: 520px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }

    /* ── CTA button ── */
    div[data-testid="column"] .stButton > button {
        background: #ffffff !important;
        color: #0b3528 !important;
        border: none !important;
        border-radius: 100px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        padding: 12px 36px !important;
        letter-spacing: 0.1px;
        transition: opacity 0.15s ease, transform 0.1s ease;
        width: 100%;
    }
    div[data-testid="column"] .stButton > button:hover {
        opacity: 0.92 !important;
        transform: translateY(-2px) !important;
    }

    /* ── Section heading ── */
    .home-sh {
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
    .home-sh::after {
        content: '';
        flex: 1;
        height: 1px;
        background: #d4e5db;
    }

    /* ── Workflow image card ── */
    [data-testid="stImage"] {
        background: #ffffff;
        border: 1px solid #dde8e2;
        border-radius: 20px;
        padding: 24px;
        overflow: hidden;
    }
    [data-testid="stImage"] img {
        border-radius: 12px;
        display: block;
        width: 100% !important;
    }

    /* ── Feature boxes ── */
    .home-feature-box {
        background: #ffffff;
        border: 1px solid #dde8e2;
        border-radius: 16px;
        padding: 28px 20px 24px;
        text-align: center;
        height: 100%;
        transition: box-shadow 0.2s ease, transform 0.2s ease;
    }
    .home-feature-box:hover {
        box-shadow: 0 8px 28px rgba(14,80,55,0.10);
        transform: translateY(-3px);
    }
    .home-feature-icon {
        font-size: 30px;
        margin-bottom: 14px;
        display: block;
    }
    .home-feature-title {
        font-size: 14.5px;
        font-weight: 600;
        color: #0b3528;
        margin-bottom: 8px;
        letter-spacing: -0.1px;
    }
    .home-feature-desc {
        font-size: 13px;
        color: #5a7868;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Hero ──
    st.markdown("""
    <div class="home-hero">
      <div class="home-hero-badge">
        <span class="home-dot"></span>
        AI-Powered · Phytochemical Screening
      </div>
      <div class="home-hero-title">
        Predict <em>Antidiabetic</em><br>Activity Instantly
      </div>
      <p class="home-hero-desc">
        AI-powered in-silico screening system trained exclusively on
        plant-derived phytochemicals for fast, reliable activity prediction.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # ── CTA Button ──
    st.markdown("<div style='margin-top:8px; margin-bottom:32px;'></div>",
                unsafe_allow_html=True)
    _, col_btn, _ = st.columns([2, 1, 2])
    with col_btn:
        if st.button("🚀 Start Prediction"):
            st.session_state.page = "prediction"
            st.rerun()

    # ── Workflow Section (FIRST) ──
    st.markdown("<div style='margin-top:8px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="home-sh">How It Works</div>', unsafe_allow_html=True)

    workflow_path = os.path.join("frontend", "img", "workflowimage.png")
    if os.path.exists(workflow_path):
        img = Image.open(workflow_path)
        st.image(img, use_container_width=True)
    else:
        st.markdown("""
        <div style="
            background:#f5f7f5;
            border: 2px dashed #bdd8c9;
            border-radius: 16px;
            padding: 48px;
            text-align: center;
            color: #6b8c7a;
            font-size: 14px;">
            📂 Place your workflow image at <code>frontend/img/workflowimage.png</code>
        </div>
        """, unsafe_allow_html=True)

    # ── Key Features (SECOND) ──
    st.markdown("<div style='margin-top:36px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="home-sh">Key Features</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="home-feature-box">
            <span class="home-feature-icon">🔬</span>
            <div class="home-feature-title">AI Engine</div>
            <div class="home-feature-desc">Random Forest–powered prediction pipeline</div>
        </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="home-feature-box">
            <span class="home-feature-icon">🌿</span>
            <div class="home-feature-title">Phytochemical Focused</div>
            <div class="home-feature-desc">Optimized for plant-derived natural compounds</div>
        </div>""", unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="home-feature-box">
            <span class="home-feature-icon">⚡</span>
            <div class="home-feature-title">Fast Screening</div>
            <div class="home-feature-desc">Single compound & batch CSV prediction</div>
        </div>""", unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="home-feature-box">
            <span class="home-feature-icon">📊</span>
            <div class="home-feature-title">Interactive Insights</div>
            <div class="home-feature-desc">Confidence scores, charts & analytics</div>
        </div>""", unsafe_allow_html=True)