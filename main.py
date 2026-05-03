import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

st.set_page_config(page_title="Offline AI Text Summarizer", layout="centered")

st.title("AI Text Summarizer (Offline)")
st.write("Summarize your text using NLP (no API required)")

text = st.text_area("Enter your text here:", height=250)

num_sentences = st.slider("Select number of sentences in summary", 1, 10, 3)

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        try:
            parser = PlaintextParser.from_string(text, Tokenizer("english"))
            summarizer = LsaSummarizer()
            summary = summarizer(parser.document, num_sentences)
            st.subheader("Summary:")
            for sentence in summary:
                st.write(sentence)
        except Exception as e:
            st.error(f"Error: {e}")
