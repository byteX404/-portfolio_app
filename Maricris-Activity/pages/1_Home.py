import streamlit as st
import datetime

st.title("🏠 Home")
st.header("Hi, I'm Maricris!")


col1, col2 = st.columns([1, 2], gap="large")


with col2:
    st.subheader("Aspiring Developer | Artist | Observer")
    st.write("""
    I am a quiet but observant individual who loves blending creativity with logic.
    Welcome to my digital workspace where I share my journey in tech and arts.
    """)
    
st.markdown("""
<style>
img {
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)