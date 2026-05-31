import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Poppins:wght@400;600;800&display=swap');
/* Light mode defaults */
body { background:#eef4ee !important; }

/* Dark mode overrides */
[data-theme="dark"] body { background:#1e1e1e !important; }

/* LOGO — as top heading, centered, prominent */
.logo-heading {
    font-family: 'Montserrat', 'Poppins', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    font-size:48px;
    font-weight:700;
    text-align:center;
    margin:2px;
    padding:2px;
    white-space:wrap;
    text-transform:none;
    letter-spacing:1.8px;
    text-shadow: 0 1px 0 rgba(255,255,255,0.02), 0 4px 18px rgba(2,48,32,0.06);
    background: linear-gradient(90deg, #092b6b 0%, #007b5e 55%);
    background-clip: text;
    -webkit-background-clip: text; /* WebKit */
    -webkit-text-fill-color: transparent; /* Ensure gradient shows on WebKit */
    color: transparent; /* Fallback for non-supporting browsers */
}
[data-theme="dark"] .logo-heading {
    text-shadow: 1px 1px 2px rgba(0,0,0,0.6), 0 1px 0 rgba(255,255,255,0.04);
    background: linear-gradient(90deg, #6BFF9A 0%, #00e080 60%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
}

.logo-accent {
    color: #00a96e;
    -webkit-text-fill-color: #00a96e;
}
.logo-tagline {
    text-align:center;
    font-family: 'Poppins', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    font-size:14px;
    color:#234b39;
    margin-top:2px;
    opacity:0.95;
}
[data-theme="dark"] .logo-tagline {
    color: #ccefd4;
    opacity:0.9;
}

/* NAV BAR — centered row */
.nav-bar {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
}

/* NAV BUTTONS — white style in light, adjusted for dark, centered */
div.stButton > button {
    background: white !important;
    border: 2px solid #00a96e !important;
    padding: 10px 26px !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    color: #00a96e !important;
    font-size: 16px !important;
    transition: 0.25s !important;
    box-shadow: 0px 0px 8px #00a96e;
    margin: 0 auto; /* Center align */
}
[data-theme="dark"] div.stButton > button {
    background: #2e2e2e !important;
    border: 2px solid #4CFF7A !important;
    color: #4CFF7A !important;
    box-shadow: 0px 0px 8px #00a96e88;
}

div.stButton > button:hover {
    background: #004aad !important;
    color: white !important;
    transform: scale(1.06);
    box-shadow: 0px 0px 15px #004aad88;
}
[data-theme="dark"] div.stButton > button:hover {
    background: #4CFF7A !important;
    color: #1e1e1e !important;
    box-shadow: 0px 0px 15px #4CFF7A88;
}

/* HERO — with CTA inside, at bottom, centered, popping up */
.hero {
    padding:70px; /* Extra bottom padding for button */
    background: linear-gradient(135deg, #004aad, #00a96e);
    border-radius:25px;
    color:white;
    text-align:center;
    box-shadow:0 8px 25px rgba(0,0,0,0.18);
    position: relative;
}
.hero h1 { font-size:55px; font-weight:900; margin:0 0 12px 0; }
.hero p { font-size:20px; opacity:0.95; margin:0; }
[data-theme="dark"] .hero {
    background: linear-gradient(135deg, #2e2e2e, #4CFF7A);
    color:#ffffff;
}

/* CTA (Start Prediction) — inside hero, at bottom, centered, green, popping up */
.hero-btn {
    background: linear-gradient(135deg, #4CFF7A, #00cc55) !important;
    color: #0b1f0b !important;
    padding: 28px 42px !important;
    border-radius: 16px !important;
    font-size: 24px !important;
    font-weight: 800 !important;
    border: none !important;
    transition: 0.25s !important;
    box-shadow: 0 0 22px #4CFF7Aaa;
    transform: scale(1);
    cursor: pointer;
    position: absolute;
    bottom: 0px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
}
[data-theme="dark"] .hero-btn {
    background: linear-gradient(135deg, #4CFF7A, #00cc55) !important;
    color: #1e1e1e !important;
    box-shadow: 0 0 22px #4CFF7Aaa;
}

.hero-btn:hover {
    transform: scale(1.08) translateX(-50%);
    box-shadow: 0 0 35px #4CFF7Add;
}

/* SQUARE FEATURE CARDS — Forces single line and square shape */
    .feature-box {
        background: white;
        width: 100%;
        aspect-ratio: 1 / 1; /* FORCES SQUARE SHAPE */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.10);
        transition: 0.3s;
        text-align: center;
        margin-top: 40px;
    }

    .feature-box:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 22px rgba(0,0,0,0.15);
    }

    .feature-icon { 
        font-size: 42px; 
        margin-bottom: 12px; 
    }

    .feature-title {
        font-weight: 700;
        font-size: 16px;
        color: #333;
        line-height: 1.2;
    }

    .feature-desc {
        font-size: 13px;
        color: #666;
        margin-top: 8px;
        font-weight: 400;
    }

/* Prediction Card */
.predict-card {
    background:white;
    padding:35px;
    border-radius:25px;
    box-shadow:0 4px 18px rgba(0,0,0,0.12);
}
[data-theme="dark"] .predict-card {
    background:#2e2e2e;
    color:#ffffff;
    box-shadow:0 4px 18px rgba(255,255,255,0.12);
}

/* Batch Buttons Sequential Layout */
.batch-buttons {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
}
[data-theme="dark"] .batch-buttons {
    /* Same as light, but ensure visibility */
}

/* Footer */
.footer {
    text-align:center;
    margin-top:45px;
    color:#444;
    padding:14px;
}
[data-theme="dark"] .footer {
    color:#cccccc;
}
    </style>
    """, unsafe_allow_html=True)
