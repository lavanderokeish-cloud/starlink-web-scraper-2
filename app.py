import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

OUTPUT_FILE = "data/daily_data_usage.csv"


def scrape_starlink(url):
    """
    Scrapes daily data usage information from a webpage.

    Modify the HTML selectors according to the actual Starlink page.
    """

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    records = []

    # Example table structure:
    # <table>
    #   <tr><th>Date</th><th>Usage</th></tr>
    #   <tr><td>2026-06-01</td><td>12.4 GB</td></tr>
    # </table>

    rows = soup.select("table tr")

    for row in rows[1:]:
        cols = row.find_all("td")

        if len(cols) >= 2:
            date = cols[0].get_text(strip=True)
            usage = cols[1].get_text(strip=True)

            records.append({
                "Date": date,
                "Data_Usage": usage
            })

    df = pd.DataFrame(records)

    os.makedirs("data", exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    return df

from flask import Flask, render_template, request
from scraper import scrape_starlink

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    table = None
    message = ""

    if request.method == "POST":

        url = request.form.get("url")

        try:
            df = scrape_starlink(url)

            if len(df) > 0:
                table = df.to_html(
                    classes="table table-striped",
                    index=False
                )
                message = "Scraping completed successfully."
            else:
                message = "No data found."

        except Exception as e:
            message = f"Error: {str(e)}"

    return render_template(
        "index.html",
        table=table,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
