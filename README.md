# Starlink Web Scraper

## An automated full-stack web scraping tool designed to log securely into a Starlink account, navigate the account dashboard, and extract dynamic daily data usage metrics directly into a structured database file.

## Features
* **Interactive WebUI:** A functional, user-friendly interface to manage the extraction process and instantly visualize data frames.
* **Automated Extraction:** Safely scrapes and parses a historical timeline of daily data usage.
* **One-Click Export:** Instantly packages the compiled data vector into a structured .csv format for data analysis.

## Installation and Setup

Follow these steps sequentially to configure your local development environment and download the required automated browser dependencies:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/syrnales/starlink-web-scraper.git
   cd starlink-web-scraper

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Install Browser Binaries:**
Initialize Playwright's core system drivers to download the headless Chromium browser infrastructure:
    ```bash
     py -m playwright install

## How to Use the Script

1. **Launch the Web Server**
   Run the following execution command in your terminal to initialize the Streamlit instance:
   ``` bash
   py -m streamlit run app.py

2. **Execute the Extraction:**

* Enter your Starlink account credentials into the allocated Username and Password interface input fields.
* Click the Start Webscraping button.
* The Playwright automation driver will launch a browser window, safely complete the authentication wall, navigate through the dashboard to your operational subscription portal, and dynamically extract your usage history timeline.

3. **Download Your Dataset:**
* Once the scraper compiles the payload, a structured visual data frame will generate directly inside the WebUI. Click the Download Data as .csv button to save the file locally as starlink_daily_usage.csv.*I
