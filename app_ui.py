import streamlit as st
from app import process_query

st.set_page_config(page_title="AI HR Assistant", page_icon="🤖", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>🤖 AI HR Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask HR-related questions instantly</p>", unsafe_allow_html=True)

# Input
user_input = st.text_input("💬 Ask your question:")

# Button
if st.button("Get Answer"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Thinking... 🤔"):
            response = process_query(user_input)

        st.markdown("### ✅ Response")
        st.success(response)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using AI")