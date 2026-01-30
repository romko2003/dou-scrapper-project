import json
from scraper.scraper import get_vacancy_links
from scraper.parser import parse_vacancy

def run_scraping():
    links = get_vacancy_links(5)
    data = [parse_vacancy(link) for link in links]

    with open("data/raw_vacancies.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(data)} vacancies")
