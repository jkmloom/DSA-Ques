import requests
import random

def fetch_stocks_free_api():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    respond = requests.get(url)
    data = respond.json()

    if data['success'] and 'data' in data:
        stocks = data['data']
        tata_stocks = stocks['data'][random.randint(0,1)]
        symbol = tata_stocks['Symbol']
        name = tata_stocks['Name']
        market_cap = tata_stocks['MarketCap']
        current_price = tata_stocks['CurrentPrice']
        return symbol, name, market_cap, current_price
    else:
        Exception("Failed to fetch stocks!")

def main():
    try:
        symbol, name, market_cap, current_price = fetch_stocks_free_api()
        print(f"\t::Stocks Data::")
        print(f"Symbol: {symbol}")
        print(f"Name: {name}")
        print(f"Market Capital: {market_cap}")
        print(f"Current Price: {current_price}")
    except Exception as exc:
        print(str(exc))

if __name__ == "__main__":
    main()