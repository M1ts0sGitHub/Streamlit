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

    # Find the specific <div align="center" with class starting with "title"
    target_div = soup.find('div', align='center', class_=lambda x: x and x.startswith('title'))
    if target_div:
        # Extract the content of the target div
        st.subheader(target_div.get_text(separator='\n', strip=True))
        content = []
        # Extract all content below the target div
        for sibling in target_div.find_next_siblings():
            if 'footer' in sibling.get('class', []) and 'hidden-xs' in sibling.get('class', []):
                break
            content.append(sibling.get_text(separator='\n', strip=True))
        text = '\n'.join(content)
    else:
        text = ""
    return text

def scrape_website(url):
    """Scrape text from the given website URL."""
    html = fetch_html(url)
    text = parse_html(html)
    return text

if __name__ == "__main__":
    today = date.today().strftime("%d/%m/%Y")  # Format: DD/MM/YYYY
    st.header(f'Rizoscraper - {today}')

    with st.expander("Rizoscraper - about"):
        st.write("This is the content inside the expander")
    

    urls = [
        f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=161",
        f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=7401",
        f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=7124",
        f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=662",
        f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=8968",
        f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=8609",
        f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=9924",
        f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=521",
        f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=9244"
    ]
    
    for url in urls:
        scraped_text = scrape_website(url)
        if scraped_text:
            st.markdown(f'<div style="text-align: justify;">{scraped_text}</div>', unsafe_allow_html=True)
            st.text("")
