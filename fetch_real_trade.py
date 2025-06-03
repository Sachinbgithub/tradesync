import requests
def fetch_real_trade(symbol):
    API_KEY = 'IGWZ7IDKT2DFGG1N'  # Replace with your actual Alpha Vantage API key
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'

    response = requests.get(url)
    data = response.json()

    if "Global Quote" in data and data["Global Quote"]:
        price = float(data["Global Quote"]["05. price"])
        quantity = 100  # Example quantity; modify as needed
        return {
            'symbol': symbol,
            'quantity': quantity,
            'price': price
        }
    else:
        raise Exception("Failed to fetch trade data from Alpha Vantage.")
