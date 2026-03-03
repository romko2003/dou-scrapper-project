import matplotlib.pyplot as plt


def plot(counter):
    techs = list(counter.keys())
    counts = list(counter.values())

    plt.figure(figsize=(12, 6))
    plt.barh(techs, counts)
    plt.title("Most demanded Python technologies (DOU.ua)")
    plt.xlabel("Vacancy count")

    plt.savefig("charts/tech_popularity.png")
    plt.show()
