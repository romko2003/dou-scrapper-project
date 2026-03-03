import json
from config import TECHNOLOGIES
from collections import Counter


def analyze():
    with open("data/raw_vacancies.json") as f:
        data = json.load(f)

    counter = Counter()

    for vac in data:
        text = vac["description"]

        for tech in TECHNOLOGIES:
            if tech.lower() in text:
                counter[tech] += 1

    return counter