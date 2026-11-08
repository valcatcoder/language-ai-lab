import streamlit as st

def analyze_text(text):
    words = text.split()
    word_count = len(words)
    characters = len(text)


    counter = 0
    for word in words:
        if len(word)>7:
            counter+=1
    long_words_count = counter
    return {
        "word_count": len(words),
        "characters": len(text),
        "long_words_count": counter
    }

           
st.title("Language AI Lab")
st.write("Welcome to my English Text Analyzer!")
text = st.text_area("Enter your English text:")
if st.button("Analyze"):
    if text.strip():
        result = analyze_text(text)
        st.subheader("Analysis results")  
        st.write("Word count:", result["word_count"])
        st.write("Character count:", result["characters"])
        st.write("Long words:", result["long_words_count"])
    else:
        st.warning("Please enter some text.")
                 
