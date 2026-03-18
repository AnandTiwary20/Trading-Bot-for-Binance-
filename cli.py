import argparse
from bot.client import get_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(args)
    except Exception as e:
        print(f"Validation Error: {e}")
        return

    client = get_client()

    print("\n--- ORDER REQUEST ---")
    print(vars(args))

    if args.type == "MARKET":
        order = place_market_order(client, args.symbol, args.side, args.quantity)
    else:
        order = place_limit_order(client, args.symbol, args.side, args.quantity, args.price)

    print("\n--- ORDER RESPONSE ---")

    if "error" in order:
        print(" Order Failed:")
        print(order["error"])
    else:
        print("Order Success:")
        print(order)


if __name__ == "__main__":
    main()