# PubMed Fetcher

A CLI tool to fetch and process research papers from PubMed, with features like filtering non-academic authors, extracting company affiliations, and exporting data to CSV files.

## Features
- Fetch papers from PubMed based on search queries.
- Extract relevant details like title, authors, journal, publication date, and DOI.
- Identify non-academic authors and company affiliations.
- Export results to CSV.
- Command-line interface with options for custom filenames, result limits, and debug mode.

## Prerequisites
- Python ≥3.12
- Poetry for dependency management

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/gitkrishna07/pumbed-fetcher.git
   cd pumbed-fetcher
   
2. Install dependencies using Poetry:
   bash
   poetry install
   

## Project Structure

pumbed_fetcher/
├── src/
│   └── pumbed_fetcher/
│       ├── __init__.py
│       ├── api.py
│       ├── cli.py
│       ├── main.py
│       ├── processing.py
│       └── utils.py
└── pyproject.toml


## Usage
Run the CLI with:
bash
poetry run get-papers-list <query> -f <output_file.csv> -n <number_of_papers> -d


### Command-line Options:

query                 Search query for PubMed articles (required)
-f, --file FILE       Output CSV file (default: papers.csv)
-n, --num NUM         Number of papers to fetch (default: 10)
-d, --debug           Enable debug mode

Example:
bash
poetry run get-papers-list "machine learning" -f papers.csv -n 5 -d


## Modules
- *api.py*: Handles API requests to PubMed.
- *cli.py*: Parses command-line arguments.
- *main.py*: Orchestrates fetching, processing, and exporting papers.
- *processing.py*: Extracts relevant paper details and saves them to CSV.
- *utils.py*: Contains helper functions.

## Development
- Use Poetry to manage dependencies.
- Follow Git version control for collaboration.

## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Commit your changes (git commit -m 'Add new feature').
4. Push the branch (git push origin feature/new-feature).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Author
- *M. Sai Krishna*  
  Email: misalesaikrishna07@gmail.com  
  GitHub: [gitkrishna07](https://github.com/gitkrishna07)  
