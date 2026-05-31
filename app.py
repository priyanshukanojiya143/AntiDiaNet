import streamlit as st
from frontend.config import set_page
from frontend.styles import load_css
from frontend.navbar import render_navbar
from frontend.home import home_page
from frontend.prediction import prediction_page
from frontend.about import about_page
from frontend.contact import contact_page
import importlib
import frontend.about
importlib.reload(frontend.about)


# ----------------------------------
# Page config + CSS
# ----------------------------------
set_page()
load_css()

# ----------------------------------
# Session state
# ----------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ----------------------------------
# Navbar
# ----------------------------------
render_navbar()

st.markdown("---")

# ----------------------------------
# Routing  ✅ FIXED (case-consistent)
# ----------------------------------
if st.session_state.page == "home":
    home_page()

elif st.session_state.page == "prediction":
    prediction_page()

elif st.session_state.page == "about":      # ✅ FIXED
    about_page()

elif st.session_state.page == "contact":    # ✅ FIXED
    contact_page()

# ----------------------------------
# Footer
# ----------------------------------
st.markdown(
    "<div class='footer'>Copyright © 2026 |ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved</div>",
    unsafe_allow_html=True
)
