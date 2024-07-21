# Pokémon Card Collection Bot

This project is designed to help you manage your Pokémon card collection by tracking which cards you have and which ones you need. It integrates with Google Sheets to keep track of your collection, scrapes prices from TCGplayer and eBay, and sends you email alerts when the prices of the cards you need drop below the average price.

## Features

- **Google Sheets Integration**: Read and update your Pokémon card collection stored in a Google Sheets document.
- **Web Scraping**: Scrape card prices from TCGplayer and eBay.
- **Price Comparison**: Compare prices from both sites and track price history over time.
- **Email Alerts**: Send email notifications when card prices drop below the average for the week or month.
- **Daily Updates**: Run the bot daily to keep your price data up to date and ensure you don't miss any good deals.

## Folder Structure

pokemon-card-bot/
├── config/
│ ├── credentials.json
│ └── settings.py
├── data/
│ ├── card_prices/
│ ├── logs/
│ └── price_history/
├── scripts/
│ ├── fetch_prices.py
│ ├── update_google_sheet.py
│ └── send_email_alert.py
├── src/
│ ├── init.py
│ ├── google_sheets.py
│ ├── scraper.py
│ ├── price_comparator.py
│ └── email_notifier.py
├── tests/
│ ├── test_google_sheets.py
│ ├── test_scraper.py
│ ├── test_price_comparator.py
│ └── test_email_notifier.py
├── .gitignore
├── README.md
├── requirements.txt
└── main.py



## Setup

### Prerequisites

- Python 3.x
- Google Cloud Platform account for Google Sheets API
- SMTP server credentials for sending email alerts

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pokemon-card-bot.git
    cd pokemon-card-bot
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up Google Sheets API:
    - Enable the Google Sheets API and create a service account.
    - Download the `credentials.json` file and place it in the `config/` folder.

4. Configure settings:
    - Update `config/settings.py` with your email server details and other configuration settings.

## Usage

1. **Fetch Prices**:
    Run the script to fetch prices from TCGplayer and eBay:
    ```sh
    python scripts/fetch_prices.py
    ```

2. **Update Google Sheets**:
    Update your Google Sheets with the current card collection data:
    ```sh
    python scripts/update_google_sheet.py
    ```

3. **Send Email Alerts**:
    Send email notifications for price alerts:
    ```sh
    python scripts/send_email_alert.py
    ```

4. **Automate Daily Run**:
    Schedule the main script to run daily using cron (Unix) or Task Scheduler (Windows):
    ```sh
    python main.py
    ```

## Contributing

Contributions are welcome! Please create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, please contact `your_email@example.com`.
