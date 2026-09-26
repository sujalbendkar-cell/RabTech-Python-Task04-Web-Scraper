"""
Data Persistence Manager for Web Scraper.
Exports structured datasets to JSON and CSV formats.
"""

import json
import csv
import os
from typing import List, Dict, Any

class DataExporter:
    @staticmethod
    def save_json(dataset: List[Dict[str, Any]], file_path: str):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dataset, f, indent=2)

    @staticmethod
    def save_csv(dataset: List[Dict[str, Any]], file_path: str):
        if not dataset:
            return
        headers = list(dataset[0].keys())
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(dataset)
