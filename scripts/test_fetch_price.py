import sys
import os

# Add the root directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from scripts.price_fetcher import fetch_card_price

def main():
    if len(sys.argv) != 3:
        print("Usage: python test_fetch_price.py <card_name> <set_name>")
        sys.exit(1)
    
    card_name = sys.argv[1]
    set_name = sys.argv[2]
    
    price = fetch_card_price(card_name, set_name)
    if price:
        print(f"The average price for {card_name} in set {set_name} is ${price:.2f}")
    else:
        print(f"Price not found for {card_name} in set {set_name}")

if __name__ == "__main__":
    main()
