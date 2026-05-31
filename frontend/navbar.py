import streamlit as st
import base64
import os

def get_img_as_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

def render_navbar():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    logo_left = get_img_as_base64("frontend/img/IASRI.png") 
    logo_right = get_img_as_base64("frontend/img/IARI.png")

    # --- Header Banner & Cursive WordArt Styling ---
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&family=Poppins:wght@800&display=swap');

        .banner-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            background: linear-gradient(to right, #ffffff, #f1f8e9, #ffffff);
            border-bottom: 4px solid #2e7d32;
            border-radius: 0 0 20px 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 35px;
        }}
        
        .banner-logo {{ height: 95px; width: auto; }}
        .banner-text {{ text-align: center; flex-grow: 1; }}

        .wordart-title {{
            font-family: 'Dancing Script', cursive; 
            font-size: 90px; 
            font-weight: 800;
            margin: 0;
            background: linear-gradient(45deg, #1b5e20, #2e7d32, #4caf50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(2px 2px 3px rgba(0,0,0,0.1));
            line-height: 0.9;
            padding-bottom: 10px;
        }}

        /* --- THE FIX: Targets ONLY the navigation area --- */
        #nav-container [data-testid="stHorizontalBlock"] {{
            display: flex;
            justify-content: center !important;
            align-items: center;
            gap: 45px !important; 
        }}

        #nav-container div.stButton > button {{
            min-width: 170px !important;
            border-radius: 12px;
            border: 2px solid #2e7d32;
            background-color: #90ee90; /* light green */
            color: white; 
            font-weight: bold;
            font-size: 17px;
            padding: 12px 20px;
            white-space: nowrap;
            transition: all 0.3s ease;
        }}

        #nav-container div.stButton > button:hover {{
            background-color: #2e7d32 !important; /* dark green on hover */
            color: green !important;
            transform: scale(1.05);
        }}
        </style>

        <div class="banner-container">
            <img src="data:image/png;base64,{logo_left}" class="banner-logo">
            <div class="banner-text">      
                <div class="wordart-title">AntiDiaNet</div>
                <h1 style="font-size: 22px; color: #333; font-family: 'serif'; margin-top: 5px;">AI-Powered In-Silico Screening of Antidiabetic Activity</h1>
                <p style="margin:0; font-size:15px; color: #666; font-family: 'Arial';">ICAR|IASRI & ICAR|IARI, NEW DELHI</p>
            </div>
            <img src="data:image/png;base64,{logo_right}" class="banner-logo">
        </div>
    """, unsafe_allow_html=True)

    # --- THE FIX: Wrap navigation columns in the nav-container div ---
    st.markdown('<div id="nav-container">', unsafe_allow_html=True)
    
    # Adjusted column ratios to ensure center alignment
    _, col1, col2, col3, col4, _ = st.columns([2, 2, 2, 2, 2, 1])

    with col1:
        if st.button("🏠 Home"):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("🧪 Prediction"):
            st.session_state.page = "prediction"
            st.rerun()
    with col3:
        if st.button("📞 Contact"):
            st.session_state.page = "contact"
            st.rerun()
    with col4:
        if st.button("🧬 About"):
            st.session_state.page = "about"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)