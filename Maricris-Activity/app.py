import streamlit as st
import base64

st.set_page_config(
    page_title="Maricris | My Portfolio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:


    st.markdown(f"""
    <style>
    .profile-container {{
        text-align: center;
        margin-top: 20px;
    }}


    .profile-name {{
        font-size: 28px;
        font-weight: bold;
        margin-top: 12px;
        color: #1f2937;
    }}

    .profile-role {{
        font-size: 14px;
        color: gray;
    }}
    </style>

    <div class="profile-container">
        <div class="profile-name">Maricris</div>
        <div class="profile-role">
            Aspiring Creator & Tech Enthusiast
        </div>
    </div>
    """, unsafe_allow_html=True)

st.title("👋 Welcome to My World")
st.markdown("---")
st.write("Navigate through my portfolio using the sidebar menu.")
st.info("Feel free to explore!")

with st.sidebar:
    st.write("Education: 3rd Year College Student (BSCS)")
    st.markdown("---")