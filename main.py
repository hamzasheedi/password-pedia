import streamlit as st
import time
from password_checker import check_password_strength
from password_gen import generate_password

#-------------------
#app
#-------------------


st.set_page_config(
    page_title="Pedia",  # Title shown on the browser tab
    page_icon="🔐",  # Favicon/icon
    layout="centered",  # Can be "wide" or "centered"
    initial_sidebar_state="collapsed"  # Can be "auto", "expanded", or "collapsed"
)

st.title("Password Pedia")
st.subheader("CHECK AND GENERATE YOUR PASSWORD")
#password
password = st.text_input("Enter your password:", type="password")

#-------------------
#pasword check
#-------------------

if password:
    st.write("🔄 Checking password strength...")  
    progress_bar = st.progress(0)  

    for percent in range(0, 101, 10):  
        time.sleep(0.2)
        progress_bar.progress(percent)

    strength, color, progress_value, suggestions = check_password_strength(password)
    progress_bar.progress(progress_value)  

    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)

    if suggestions:
        st.write("### 🔍 Suggestions to Improve Your Password:")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")

#-------------------
#password genator
#-------------------

st.write("---")  # Horizontal Line
st.subheader("🔑 Generate a Secure Password")

password_length = st.slider("Select Password Length", min_value=8, max_value=32, value=12)
if st.button("🔄 Generate Password"):
    new_password = generate_password(password_length)
    if new_password:
        st.success(f"**Generated Password:** `{new_password}`")
        st.code(new_password, language="text")