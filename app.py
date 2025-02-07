import streamlit as st
from langchain_ollama import OllamaLLM
from bots import bots 

# Streamlit UI
st.title("Newsletter to Blog Converter")
st.write("Enter the newsletter text below, and the system will generate a blog post.")

newsletter_input = st.text_area("Newsletter Text", height=300)

st.cache_data.clear()
    
if st.button("Generate Blog"):
    if newsletter_input.strip():
        with st.spinner("Generating blog..."):
            blog_output = bots.generate_blog(newsletter_input)
            st.subheader("Generated Blog:")
            st.write(blog_output)
    else:
        st.warning("Please enter some text to generate a blog.")
        
