### Rizoscraper 2024 ###

import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import date

def fetch_html(url):
    """Fetch the HTML content of the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

def parse_html(html):
    """Parse the HTML content and extract text from and below <div align="center" class="title*">, excluding <div class="footer hidden-xs">."""
    soup = BeautifulSoup(html, 'html.parser')
    content = []

    # Find the specific <div align="center" with class starting with "title"
    target_div = soup.find('div', align='center', class_=lambda x: x and x.startswith('title'))
    if target_div:
        # Extract the content of the target div
        title = target_div.get_text(separator='\n', strip=True)
        # Extract all content below the target div
        for sibling in target_div.find_next_siblings():
            if 'footer' in sibling.get('class', []) and 'hidden-xs' in sibling.get('class', []):
                break
            content.append(sibling.get_text(separator='\n', strip=True))
        article = '\n'.join(content)
    else:
        title = ""
        article = ""
    return title, article

def scrape_website(url):
    """Scrape text from the given website URL."""
    html = fetch_html(url)
    text = parse_html(html)
    return text

if __name__ == "__main__":

    ### Data ###
    today = date.today().strftime("%d/%m/%Y")  # Format: DD/MM/YYYY

    urls = [
    (f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=161", "Από μέρα σε μέρα"),
    (f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=7401", "Η 'Αποψη μας"),
    (f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=7124", "Αποκαλυπτικά"),
    (f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=662", "test"),
    (f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=8968", "test"),
    (f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=8609", "test"),
    (f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=9924", "test"),
    (f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=521", "test"),
    (f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=9244", "test")
    ]

    
    
    st.title('Rizoscraper')
    st.write("Welcome to our site! We leverage the power of Python to bring you the latest news articles from Rizospastis.gr. Our custom scraper, built with BeautifulSoup and requests, efficiently gathers specific articles from Rizospastis.gr. Using Streamlit, we present this curated content in a user-friendly and interactive format. Stay informed with our quick, daily, and streamlined news feed!")

    st.text("")
    st.header(f'{today} - Articles from Rizospastis.gr')
    
    for url in urls:
        title, article = scrape_website(url[0])
        if article:
            with st.expander(url[1]):
                st.write(title)
                st.write(url[0])
                st.markdown(f'<div style="text-align: justify;">{article}</div>', unsafe_allow_html=True)
