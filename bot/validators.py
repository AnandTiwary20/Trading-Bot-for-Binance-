def validate_order(args):
    if args.quantity <= 0:
        raise ValueError("Quantity must be positive")

    if args.side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT order")