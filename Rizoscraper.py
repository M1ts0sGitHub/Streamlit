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
        st.subheader = [target_div.get_text(separator='\n', strip=True)]
        content = ""
        # Extract all content below the target div
        for sibling in target_div.find_next_siblings():
            if 'footer' in sibling.get('class', []) and 'hidden-xs' in sibling.get('class', []):
                break
            content.append(sibling.get_text(separator='\n', strip=True))
        text = '\n'.join(content)
    else:
        text = "No content found."
    st.text(text)

def scrape_website(url):
    """Scrape text from the given website URL."""
    html = fetch_html(url)
    text = parse_html(html)
    return text

if __name__ == "__main__":
    today = date.today().strftime("%d/%m/%Y")  # Format: DD/MM/YYYY
    st.header(f'Rizoscraper - {today})

    url = [f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=161",
           f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=7401",
           f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=7124",
           f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=662",
           f"https://www.rizospastis.gr/columnPage.do?publDate={today}&columnId=8968",
           f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=8609",
           f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=9924",
           f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=521",
           f"https://www.rizospastis.gr/columnStory.do?publDate={today}&columnId=9244"]
    for url in url:
    # print(url)
        scraped_text = scrape_website(url)
        # print(scraped_text)


# There are several options for deploying your Python script to run automatically every morning. Here are a few popular choices:

# Google Cloud Platform (GCP) - Cloud Scheduler:

# Cloud Scheduler is a fully managed cron job service that allows you to schedule virtually any job, including HTTP/S endpoints and Pub/Sub topics.
# You can deploy your Python script as a Cloud Function and use Cloud Scheduler to trigger it at a specific time each day1.
# AWS Lambda with Amazon CloudWatch Events:

# AWS Lambda lets you run code without provisioning or managing servers. You can set up a CloudWatch Event to trigger your Lambda function on a schedule.
# This is a good option if you're already using AWS services.
# Azure Functions with Timer Trigger:

# Azure Functions can be triggered by a timer, making it easy to run your Python script on a schedule.
# You can define a cron expression to specify the schedule.
# GitHub Actions:

# GitHub Actions allows you to automate workflows directly from your GitHub repository.
# You can set up a workflow to run your Python script on a schedule using cron syntax2.
# Heroku Scheduler:

# Heroku Scheduler is an add-on for running scheduled tasks on your Heroku apps.
# You can use it to run your Python script at specific times.
# Cron Jobs on a VPS:

# If you have a Virtual Private Server (VPS), you can set up a cron job to run your Python script at a specified time.
# This is a more manual approach but gives you full control over the environment.
# Each of these options has its own setup process and requirements. If you need detailed steps for any specific platform, let me know, and I can provide more information!
