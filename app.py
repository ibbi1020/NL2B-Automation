import streamlit as st
from src.bots import blog_generator, visual_generator

def main():
    st.title("Newsletter to Blog Converter (NEW)")
    st.write("Enter the newsletter text below, and the system will generate a blog post.")

    newsletter_input = st.text_area("Newsletter Text", height=300)
    st.cache_data.clear()
    
    if st.button("Generate Blog"):
        if newsletter_input.strip():
            with st.spinner("Generating blog..."):
                blog_output = blog_generator.generate_blog(newsletter_input)
                visual_generator.generate_visuals(blog_output)
                st.subheader("Visuals saved to output folder")
        else:
            st.warning("Please enter some text to generate a blog.")

if __name__ == "__main__":
    main()