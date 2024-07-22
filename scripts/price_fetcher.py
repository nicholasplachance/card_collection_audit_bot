import requests
from config.settings import POKEMON_TCG_API_KEY

API_URL = "https://api.pokemontcg.io/v2/cards"

def fetch_card_price(card_name, set_name):
    headers = {
        'X-Api-Key': POKEMON_TCG_API_KEY
    }
    params = {
        'q': f'name:{card_name} set.name:{set_name}'
    }
    response = requests.get(API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        card_data = response.json()
        if card_data['data']:
            prices = card_data['data'][0].get('cardmarket', {}).get('prices', {})
            return prices.get('averageSellPrice')
        else:
            print(f"No price data found for card: {card_name} in set: {set_name}")
            return None
    else:
        print(f"Failed to fetch price data for card: {card_name}. Status code: {response.status_code}")
        return None
