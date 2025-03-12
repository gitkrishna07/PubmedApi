import argparse
import csv
from pumbed_fetcher.api import fetch_papers, fetch_paper_details
from pumbed_fetcher.utils import PaperProcessor

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Fetch and process PubMed papers.")
    parser.add_argument("query", type=str, help="Search query for PubMed articles")
    parser.add_argument("-f", "--file", type=str, default="results.csv", help="Output CSV file")
    parser.add_argument("-n", "--num", type=int, default=10, help="Number of papers to fetch")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    return parser.parse_args()

def main():
    """Handle CLI execution."""
    args = parse_arguments()
    paper_ids = fetch_papers(args.query, args.num, debug=args.debug)
    
    if not paper_ids:
        print("No papers found.")
        return

    papers = {pid: fetch_paper_details(pid, debug=args.debug) for pid in paper_ids}
    
    processor = PaperProcessor({"uids": paper_ids, **papers})
    processed_data = processor.extract_relevant_details()
    
    if not processed_data:
        print("No relevant data extracted.")
        return
    
    with open(args.file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=processed_data[0].keys())
        writer.writeheader()
        writer.writerows(processed_data)
    
    print(f"Results saved to {args.file}")

if __name__ == "__main__":
    main()








