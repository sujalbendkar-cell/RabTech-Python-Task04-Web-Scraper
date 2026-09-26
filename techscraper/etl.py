"""
ETL Data Transformer & Summary Statistics Reporter.
"""

from typing import List, Dict, Any

class ETLProcessor:
    @staticmethod
    def transform_dataset(raw_articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Clean and transform raw scraped dataset."""
        cleaned = []
        for item in raw_articles:
            title = item.get("title", "").strip()
            points = int(item.get("points", 0))
            category = item.get("category", "General")
            
            # Simple sentiment/relevance tagging
            if any(k in title.lower() for k in ["cyber", "security", "threat", "vulnerability"]):
                category = "Cybersecurity"
            elif any(k in title.lower() for k in ["python", "code", "etl", "scraping"]):
                category = "Python / Dev"

            cleaned.append({
                "id": item.get("id"),
                "title": title,
                "url": item.get("url"),
                "points": points,
                "author": item.get("author", "Unknown"),
                "category": category
            })

        # Sort by points descending
        cleaned.sort(key=lambda x: x["points"], reverse=True)
        return cleaned

    @staticmethod
    def generate_summary_report(dataset: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate summary statistics report upon execution."""
        total_items = len(dataset)
        if total_items == 0:
            return {"total_items": 0, "avg_points": 0, "top_category": "None"}

        total_points = sum(item["points"] for item in dataset)
        avg_points = round(total_points / total_items, 2)
        top_item = max(dataset, key=lambda x: x["points"])

        categories = {}
        for item in dataset:
            c = item["category"]
            categories[c] = categories.get(c, 0) + 1

        top_cat = max(categories, key=categories.get)

        return {
            "total_items": total_items,
            "total_points": total_points,
            "avg_points": avg_points,
            "top_article": top_item["title"],
            "top_article_points": top_item["points"],
            "category_distribution": categories,
            "top_category": top_cat
        }
