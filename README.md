# LinkedIn Scraper

This project is a LinkedIn data scraper built using Python's Selenium and
Beautiful Soup libraries. It allows users to search for specific technology
stacks on LinkedIn, extract relevant job and people data, and save the results
into a `.txt` file.

## Prerequisites

-  Python must be installed on your system. You can download it from
   [python.org](https://www.python.org/).
-  Ensure you have `pip` installed for managing Python packages.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/NjauSamuel/LinkedIn-Python-Web-Scraper.git
   cd linkedin-scraper
   ```

2. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Rename the `credentials_template.txt` file located in the project directory
   to `credentials.txt`.

2. Enter your LinkedIn login credentials:

   -  **Line 1**: Your LinkedIn email.
   -  **Line 2**: Your LinkedIn password.

3. Save the `credentials.txt` file.

## Usage

1. Run the Python script:

   ```bash
   python main.py
   ```

2. When prompted in the terminal, input the technology stack you want to search
   for on LinkedIn. For example, you can type:

   ```bash
   Python
   ```

   or

   ```bash
   PHP
   ```

3. The program will then scrape LinkedIn for job listings and people associated
   with the given stack, and save the output to a `.txt` file in the project
   directory.

## Output

-  The scraped data, including relevant job postings and LinkedIn profiles, will
   be saved into a `.txt` file for you to review.

## Author

[Samuel Njau](https://www.linkedin.com/in/samuel-njau/)
