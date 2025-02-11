import streamlit as st
from bots import bots_local 
from bots import bots

# Streamlit UI
st.title("Newsletter to Blog Converter (NEW)")
st.write("Enter the newsletter text below, and the system will generate a blog post.")

newsletter_input = st.text_area("Newsletter Text", height=300)

st.cache_data.clear()
    
if st.button("Generate Blog"):
    if newsletter_input.strip():
        with st.spinner("Generating blog..."):
            blog_output = bots.generate_blog(newsletter_input)
            #st.subheader("Generated Blog:")
            #st.write(blog_output)
            
            #metadata_output = bots.generate_metadata(blog_output)
            #st.subheader("Generated Metadata: ")
            #st.write(metadata_output)
            
            bots.generate_visuals(blog_output)
            st.subheader("Visuals saved to output folder")
    else:
        st.warning("Please enter some text to generate a blog.")
        
