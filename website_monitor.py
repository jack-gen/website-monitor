# -*- coding: utf-8 -*-
"""Website Monitor

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ENqSse32cDSyZf3uocqNEnq7-MeZUp-O
"""

import requests
from bs4 import BeautifulSoup
import os.path
from datetime import datetime, timedelta

# Function to scrape HTML content from a URL
def scrape_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to save HTML content to a file with the current date in the filename
def save_html_with_date(html_content, url):
    # Get current date and time
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Generate filename with date and URL
    filename = f"{current_date}_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.html"
    with open(filename, "w") as file:
        file.write(html_content)

# Function to compare two HTML contents
def compare_html(old_html, new_html):
    # Compare old and new HTML content
    # You can use difflib or any other method for comparison
    # For simplicity, let's just compare the strings
    if old_html == new_html:
        return False
    else:
        return True

# Main function
def main():
    # Title of the web app
    st.title("Website Content Monitoring")

    # Input field for the URL
    url = st.text_input("Enter the URL to monitor")

    # Button to trigger scraping and comparison
    if st.button("Monitor"):
        if url:
            new_html = scrape_html(url)
            if new_html:
                # Save HTML content with date and URL in the filename
                save_html_with_date(new_html, url)
                # Display the HTML content
                st.text(new_html)

                # Compare HTML content with previous day
                current_date = datetime.now().strftime("%Y-%m-%d")
                today_filename = f"{current_date}_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.html"
                yesterday = datetime.now() - timedelta(days=1)
                yesterday_date = yesterday.strftime("%Y-%m-%d")
                yesterday_filename = f"{yesterday_date}_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.html"
                # Compare HTML content if yesterday's file exists
                if os.path.exists(yesterday_filename):
                    with open(today_filename, "r") as file:
                        today_html = file.read()
                    with open(yesterday_filename, "r") as file:
                        yesterday_html = file.read()
                    if compare_html(today_html, yesterday_html):
                        st.text("Changes detected!")
                    else:
                        st.text("No changes")
            else:
                st.text("Unable to fetch HTML content.")
        else:
            st.text("Please enter a URL.")

if __name__ == "__main__":
    main()