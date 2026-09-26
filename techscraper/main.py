"""
CLI Main Entry Point for TechScraper ETL Pipeline.
"""

import sys
import argparse
import os
import time
from techscraper.scraper import WebScraperEngine
from techscraper.etl import ETLProcessor
from techscraper.persistence import DataExporter

def main():
    parser = argparse.ArgumentParser(
        prog="techscraper",
        description="Automated Web Scraping & Data Extraction ETL Pipeline"
    )
    parser.add_argument("--url", type=str, default="https://news.ycombinator.com", help="Target URL to scrape")
    parser.add_argument("--json", type=str, default="scraped_data.json", help="Output JSON path")
    parser.add_argument("--csv", type=str, default="scraped_data.csv", help="Output CSV path")
    parser.add_argument("--delay", type=float, default=1.0, help="Rate limiting delay in seconds")

    args = parser.parse_args()

    start_time = time.time()
    print("==================================================")
    print("  🕷️ TECHSCRAPER - AUTOMATED ETL WEB SCRAPER")
    print("==================================================")
    print(f" Target URL: {args.url}")
    print(f" Rate Limiting Delay: {args.delay}s | Custom Headers: Enabled")
    print("--------------------------------------------------")

    # 1. Fetch & Parse
    print("\n🌐 Fetching web page and parsing HTML structure...")
    scraper = WebScraperEngine(delay_seconds=args.delay)
    html = scraper.fetch_page(args.url)
    raw_data = scraper.parse_hacker_news(html)

    # 2. Transform (ETL)
    print("⚙️ Processing ETL Transformations & Categorization...")
    clean_data = ETLProcessor.transform_dataset(raw_data)
    summary = ETLProcessor.generate_summary_report(clean_data)

    # 3. Export to JSON & CSV
    DataExporter.save_json(clean_data, args.json)
    DataExporter.save_csv(clean_data, args.csv)
    print(f"\n✅ Exported {len(clean_data)} items to JSON: {os.path.abspath(args.json)}")
    print(f"✅ Exported {len(clean_data)} items to CSV:  {os.path.abspath(args.csv)}")

    # 4. Print Summary Statistics Report
    elapsed = round(time.time() - start_time, 2)
    print("\n--------------------------------------------------")
    print("  📊 AUTOMATED SUMMARY STATISTICS REPORT")
    print("--------------------------------------------------")
    print(f" Total Articles Scraped: {summary['total_items']}")
    print(f" Total Score Points:      {summary['total_points']}")
    print(f" Average Score Points:    {summary['avg_points']}")
    print(f" Top Article:             {summary['top_article']} ({summary['top_article_points']} pts)")
    print(f" Top Category:            {summary['top_category']}")
    print(f" Category Breakdown:      {summary['category_distribution']}")
    print(f" Total Execution Time:    {elapsed} seconds")
    print("==================================================")

if __name__ == "__main__":
    main()
