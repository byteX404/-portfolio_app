import streamlit as st

st.title("🎮 Hobbies & Interests")
st.write("When I'm not learning, I'm relaxing or strategizing.")

hobbies = [
    ("🎬 Watching Movies & Anime", "Love exploring different genres of film and animation."),
    ("♟️ Strategy Games", "Enjoying chess and tactical word games to sharpen the mind."),
    ("📚 Reading Books", "Expanding knowledge through various literature."),
    ("🕵️ Digital Exploration", "Discovering new tech trends and digital tools.")
]

for hobby, desc in hobbies:
    with st.expander(hobby):
        st.write(desc)

st.markdown("---")
st.subheader("🎯 What I enjoy most")
st.write("""
I love the balance between sitting back watching a good anime and actively 
playing a strategic chess game. It keeps both sides of my brain active!
""")