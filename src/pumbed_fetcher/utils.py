import csv
import json

class PaperProcessor:
    def __init__(self, data):
        """Initialize with paper data."""
        self.data = data

    def extract_relevant_details(self):
        """Extract necessary details from the raw PubMed data."""
        extracted_data = []
        for uid in self.data.get("uids", []):
            paper = self.data.get(uid, {})
            extracted_data.append({
                "ID": paper.get("uid", ""),
                "Title": paper.get("title", ""),
                "Authors": ", ".join([author.get("name", "") for author in paper.get("authors", [])]),
                "Publication Date": paper.get("pubdate", ""),
                "Journal": paper.get("source", ""),
                "DOI": next((id["value"] for id in paper.get("articleids", []) if id["idtype"] == "doi"), "")
            })
        return extracted_data

    def save_to_csv(self, filename):
        """Save extracted data to a CSV file."""
        data = self.extract_relevant_details()
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Title", "Authors", "Publication Date", "Journal", "DOI"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}")

# Example usage:
if __name__ == "__main__":
    with open("sample_data.json", "r") as f:
        raw_data = json.load(f)

    processor = PaperProcessor(raw_data)
    processor.save_to_csv("papers.csv")
