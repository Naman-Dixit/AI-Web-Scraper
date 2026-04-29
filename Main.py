import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama

st.set_page_config(page_title="AI Web Scraper", layout="wide")
st.title("🕵️‍♂️ AI Web Scraper")

url = st.text_input("Enter Website URL (include http://)")

if st.button("Step 1: Scrape & Clean"):
    if url:
        with st.spinner("Scraping..."):
            dom_content = scrape_website(url)
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)
            
            st.session_state.dom_content = cleaned_content
            st.success("Scraping complete!")
            
            with st.expander("View Cleaned Content"):
                st.text_area("Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("What do you want to extract? (e.g., 'List all prices', 'Find the contact email')")

    if st.button("Step 2: AI Parse"):
        if parse_description:
            with st.spinner("AI is thinking..."):
                dom_chunks = split_dom_content(st.session_state.dom_content)
                result = parse_with_ollama(dom_chunks, parse_description)
                st.subheader("Results:")
                st.write(result)