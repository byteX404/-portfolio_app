import streamlit as st

st.title("⚡ Skills")
st.write("Here are the core competencies I bring to the table.")

st.markdown("### 🎨 Creativity & Arts")
st.progress(95)
st.caption("High proficiency in creative design and artistic thinking.")

st.markdown("### 🧩 Problem Solving")
st.progress(85)
st.caption("Analytical thinking and solution-oriented approach.")

st.markdown("### 🖥️ Tech & Digital")
st.progress(70)
st.caption("Exploring technology and digital tools.")

st.markdown("### 🤝 Adaptability")
st.progress(90)
st.caption("Quick learner who adapts easily to new environments.")

st.markdown("---")
m1, m2, m3 = st.columns(3)
m1.metric("Creativity", "High", "")
m2.metric("Adaptability", "High", "")
m3.metric("Learning", "Ongoing", "")