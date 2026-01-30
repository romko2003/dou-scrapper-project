# Python Technologies Statistics (DOU.ua)

This project combines **Web Scraping** and **Data Analysis** to analyze the most in-demand technologies in Python job vacancies on **dou.ua**.

The goal is to help Python developers understand which technologies are currently most required on the job market, so they can prioritize what to learn and prepare better for interviews.

---

## 🚀 Project Overview

The project:
- Scrapes public Python job vacancies from dou.ua  
- Extracts technologies mentioned in job descriptions  
- Counts how frequently each technology appears  
- Visualizes popularity statistics using charts  
- Stores historical results to track trends over time  

---

## 🧱 Project Architecture

The project is split into **two independent parts** (Single Responsibility Principle):

### 1️⃣ Scraping Module
- Collects vacancy links
- Downloads job descriptions
- Saves raw vacancy data into JSON

### 2️⃣ Data Analysis Module
- Loads stored vacancy data
- Analyzes technology mentions
- Builds statistics & charts
- Saves visualization results

---

## 🛠 Technologies Used

- Python  
- Requests  
- BeautifulSoup  
- Pandas  
- Matplotlib  
- SQLite (optional storage)  
- Asyncio (optional performance upgrade)  
- NLP tools (optional: nltk, wordcloud)  

---

## 📊 Example Output

The project generates charts showing the **most demanded technologies**:

![Technology Popularity Chart](charts/tech_popularity.png)

---

## ⚙️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/py-dou-tech-stats.git
cd py-dou-tech-stats
2. Install dependencies
pip install -r requirements.txt
3. Run the scraper & analysis
python main.py
📁 Project Structure
py-dou-tech-stats/
│
├── scraper/           # Scraping logic
├── analysis/          # Data processing & charts
├── data/              # Raw scraped vacancies
├── charts/            # Generated visualizations
├── config.py          # Technology list & settings
├── main.py            # Project entry point
└── README.md
📌 Configuration
You can modify tracked technologies in config.py:

TECHNOLOGIES = [
    "Python", "Django", "Flask", "FastAPI",
    "PostgreSQL", "Docker", "AWS",
    "Redis", "Celery", "Pandas"
]
📈 Additional Features (Optional Enhancements)
Async scraping for performance

NLP-based technology extraction (no static config)

WordCloud visualization

Experience level segmentation (Junior / Middle / Senior)

Market trend tracking over time

Salary & popularity correlation analysis

⚠️ Disclaimer
Only public job data is scraped

No authentication is used

No private user data is collected

Scraping respects legal and ethical standards

👨‍💻 Author
Roman Azhniuk
Mate Academy — Python Track

⭐ Why This Project Matters
This project helps developers:

Understand real job market demand

Make informed learning decisions

Build strong portfolio projects

Gain real-world scraping & analytics experience
