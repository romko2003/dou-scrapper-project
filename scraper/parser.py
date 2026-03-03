import requests
from bs4 import BeautifulSoup


def parse_vacancy(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    title = soup.select_one("h1").text.strip()
    description = soup.select_one(".vacancy-section").text.lower()

    return {
        "title": title,
        "url": url,
        "description": description
    }