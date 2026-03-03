import requests
from bs4 import BeautifulSoup
from config import BASE_URL, HEADERS


def get_vacancy_links(pages=3):
    links = []

    for page in range(1, pages + 1):
        url = f"{BASE_URL}&page={page}"
        resp = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.text, "html.parser")

        for a in soup.select(".vt a"):
            links.append(a["href"])

    return links