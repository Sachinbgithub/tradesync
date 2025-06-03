import requests

def fetch_real_trades(symbol="AAPL"):
    API_KEY = "IGWZ7IDKT2DFGG1N"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY" \
          f"&symbol={symbol}&interval=1min&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    latest_time = list(data["Time Series (1min)"].keys())[0]
    latest_data = data["Time Series (1min)"][latest_time]
    
    price = float(latest_data["1. open"])
    quantity = 100  # simulate a quantity
    
    return {
        "symbol": symbol,
        "quantity": quantity,
        "price": price
    }
