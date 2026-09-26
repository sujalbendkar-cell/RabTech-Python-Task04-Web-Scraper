# 🕷️ TechScraper - Automated Web Scraping & Data Extraction ETL Pipeline

**Developer:** Sujal Bendkar | **ID:** `RAB-2026-9471669A59`  
**Track:** Python Software Engineering (RabTech Academy)  
**Task 04:** Automated Web Scraping & Data Extraction Pipeline  

---

## 📌 Project Overview
`techscraper` is a production-grade, automated ETL web scraping pipeline built in Python using `BeautifulSoup4` and `requests`. It extracts structured datasets from live web resources, implements rate limiting and retry logic with exponential backoff, transforms raw HTML into structured JSON & CSV formats, and generates an automated summary statistics report upon execution.

---

## 🛠️ Features & Architecture

* **🕷️ Robust Web Scraper:** Custom User-Agent headers, rate limiting (`time.sleep`), and retry logic to follow web scraping best practices.
* **⚙️ ETL Data Pipeline:** Parses raw HTML DOM elements, cleans titles, extracts point scores/authors, and categorizes entries automatically.
* **💾 Data Persistence:** Exports dataset to both structured **JSON** (`scraped_data.json`) and **CSV** (`scraped_data.csv`).
* **📊 Automated Summary Statistics:** Calculates total items scraped, score averages, top category breakdown, and execution runtime.
* **🧪 Unit Testing Suite:** Automated tests covering fallback parsers, ETL transformations, and analytical report calculations.

---

## 🚀 Quick Start & Usage

```bash
# 1. Install dependencies
pip install -r requirements.txt
pip install -e .

# 2. Run Web Scraper & ETL Pipeline
python run_scraper.py
# OR
techscraper

# 3. Run Automated Unit Tests
python -m unittest discover tests
```

---

## 📋 Repository Structure
```text
RabTech-Python-Task04-Web-Scraper/
├── pyproject.toml                     # Package setup manifest
├── requirements.txt                   # Dependency list (beautifulsoup4, requests)
├── README.md                          # Documentation
├── run_scraper.py                     # One-click launcher script
├── techscraper/                       # Main Python package
│   ├── __init__.py                    # Version metadata
│   ├── scraper.py                     # Scraper engine (rate limiting, retries, headers)
│   ├── etl.py                         # ETL transformer & summary statistics reporter
│   ├── persistence.py                 # JSON & CSV exporter
│   └── main.py                        # CLI entry point
└── tests/                             # Unit tests
    └── test_scraper.py                # Unit test suite
```

---

## 👤 Author & Credits
* **Developer:** Sujal Bendkar
* **Batch:** `BATCH-SEP-2026`
* **Academy:** RabTech Academy - Python Software Engineering Internship
