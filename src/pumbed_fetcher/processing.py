import csv
import json
from pumbed_fetcher.utils import PaperProcessor

def process_and_save_papers(raw_data, filename):
    """Process paper data and save to CSV."""
    processor = PaperProcessor(raw_data)
    extracted_data = processor.extract_relevant_details()

    if not extracted_data:
        print("No relevant data extracted.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=extracted_data[0].keys())
        writer.writeheader()
        writer.writerows(extracted_data)

    print(f"Data saved to {filename}")

# Example usage:
if __name__ == "__main__":
    with open("sample_data.json", "r") as f:
        raw_data = json.load(f)

    process_and_save_papers(raw_data, "papers.csv")






