import streamlit as st

st.title("🧑‍💻 About Me")
st.markdown("### Who I Am")

st.write("""
I love learning new things and improving my skills every day. I am quiet but observant, 
easy to work with, and I adapt quickly to new changes. I truly believe in the power of 
combining creativity with technical knowledge.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🎨 My Creative Side")
    st.write("- Love for Arts & Design")
    st.write("- Watching Anime & Movies")
    st.write("- Playing Strategy Games")

with col2:
    st.markdown("#### 💻 My Tech Side")
    st.write("- Digital Exploration")
    st.write("- Problem Solving")
    st.write("- Web Development Interest")

st.markdown("---")
st.subheader("⚡ Personality")
st.write("""
*'I am always happy to work with a team. I love combining my creative and artistic side 
with my love for learning how things work.'*
""")