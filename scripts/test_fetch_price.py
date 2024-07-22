import sys
import os

# Add the root directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from scripts.price_fetcher import fetch_card_price

if __name__ == "__main__":
    card_name = "Charizard"  # Example card name, you can change it to test other cards
    price = fetch_card_price(card_name)
    if price:
        print(f"The average price for {card_name} is ${price:.2f}")
    else:
        print(f"Price not found for {card_name}")
