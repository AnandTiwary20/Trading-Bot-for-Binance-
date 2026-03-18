from client import get_client
from logger import setup_logger
from orders import place_market_order, place_limit_order

def main():
    setup_logger()

    client = get_client()

    symbol = "BTCUSDT"
    quantity = 0.001

    place_market_order(client, symbol, "BUY", quantity)
    place_limit_order(client, symbol, "SELL", quantity, price="70000")

if __name__ == "__main__":
    main()

# place_market_order(client, symbol, "BUY", quantity)
# place_limit_order(client, symbol, "SELL", quantity, price="70000")