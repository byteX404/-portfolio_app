import streamlit as st

st.title("📞 Contact Me")
st.write("Feel free to reach out for collaborations or just to chat!")

st.markdown("""
**📱 Phone:** 09853722554  
**📧 Email:** gludomc11@gmail.com  
**📘 Facebook:** [Cris Ra](https://www.facebook.com/cris.ra.583951)  
**📸 Instagram:** @gludomc11
""")

st.markdown("---")
st.subheader("✉️ Send a Message")

# Simple Form Logic
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        if name and email and message:
            st.success(f"Thanks {name}! Message sent successfully. ✅")
        else:
            st.error("Please fill in all fields.")

st.markdown("---")
st.caption("© Maricris Portfolio")