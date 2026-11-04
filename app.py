import streamlit as st
st.title("Language AI Lab")
st.write("Welcome to my English Text Analyzer!")
text = st.text_area("Enter your English text:")
if st.button("Analyze"):
    st.write("Your text:", text)
