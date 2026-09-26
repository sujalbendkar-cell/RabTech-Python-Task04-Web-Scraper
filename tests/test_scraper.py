"""
Unit Test Suite for Web Scraper & ETL Pipeline.
"""

import unittest
from techscraper.scraper import WebScraperEngine
from techscraper.etl import ETLProcessor

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraperEngine(delay_seconds=0.1)

    def test_fallback_dataset(self):
        dataset = self.scraper._get_fallback_dataset()
        self.assertGreater(len(dataset), 0)
        self.assertIn("title", dataset[0])

    def test_etl_transform(self):
        raw = [
            {"id": 1, "title": "Python Cyber Security Threat Analysis", "points": 100, "author": "tester"}
        ]
        clean = ETLProcessor.transform_dataset(raw)
        self.assertEqual(clean[0]["category"], "Cybersecurity")

    def test_summary_report(self):
        clean = [
            {"id": 1, "title": "Article A", "points": 50, "category": "Tech News"},
            {"id": 2, "title": "Article B", "points": 150, "category": "Python"}
        ]
        summary = ETLProcessor.generate_summary_report(clean)
        self.assertEqual(summary["total_items"], 2)
        self.assertEqual(summary["avg_points"], 100.0)

if __name__ == "__main__":
    unittest.main()
