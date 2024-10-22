import streamlit as st

st.title("Web Scraping-based AI Web app")
url = st.text_input("Enter a website url: ")

if st.button("Scrape site"):
    st.write("Scraping the website")