import requests

# Replace with your actual PriceCharting API key
PRICE_CHARTING_API_KEY = 'your_price_charting_api_key_here'

# Define the API endpoint and parameters
API_URL = "https://www.pricecharting.com/api/product"
API_KEY = 'c0b53bce27c1bdab90b1605249e600dc43dfd1d5'
PRODUCT_ID = 'charizard #4'

# Prepare the headers with the API key
headers = {
    'Authorization': f'Bearer {PRICE_CHARTING_API_KEY}'
}

# Define the parameters for the request
params = {
    't': API_KEY,
    'q': PRODUCT_ID
}

# Make the GET request to the API
response = requests.get(API_URL, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    product_data = response.json()
    print(product_data)
else:
    print(f"Failed to fetch product data. Status code: {response.status_code}")
