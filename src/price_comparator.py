from src.google_sheets import get_set_data
from src.price_fetcher.py import fetch_card_price

def compare_prices(set_name=None):
    collection_data = get_set_data(set_name)
    if not collection_data:
        print("No data found in the collection.")
        return

    price_differences = {}

    for set_name, cards in collection_data.items():
        print(f"\nComparing prices for set: {set_name}")
        for card in cards:
            card_name = card['Name']
            card_price = fetch_card_price(card_name)
            if card_price:
                collection_price = float(card.get('Price', 0))
                if collection_price > card_price:
                    price_differences[card_name] = {
                        'collection_price': collection_price,
                        'current_price': card_price,
                        'difference': collection_price - card_price
                    }
    
    return price_differences

# Example usage
if __name__ == "__main__":
    set_name = "Jungle Set List"  # or leave None to compare all sets
    differences = compare_prices(set_name)
    if differences:
        for card_name, prices in differences.items():
            print(f"\nCard: {card_name}")
            print(f"Collection Price: ${prices['collection_price']:.2f}")
            print(f"Current Price: ${prices['current_price']:.2f}")
            print(f"Difference: ${prices['difference']:.2f}")
    else:
        print("No price differences found.")
