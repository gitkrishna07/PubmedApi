import csv
from pumbed_fetcher.api import fetch_papers, fetch_paper_details
from pumbed_fetcher.cli import parse_arguments
from pumbed_fetcher.processing import PaperProcessor


def main():
    """Main function to fetch and process PubMed papers."""
    args = parse_arguments()
    paper_ids = fetch_papers(args.query, args.num, debug=args.debug)

    if not paper_ids:
        print("No papers found for the given query.")
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



