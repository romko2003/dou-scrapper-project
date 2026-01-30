from scraper.save_raw_data import run_scraping
from analysis.analyzer import analyze
from analysis.charts import plot

run_scraping()
counter = analyze()
plot(counter)