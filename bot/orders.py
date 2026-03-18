
import logging 

def place_market_order(client, symbol, side, quantity):
    try: 
        order =client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market order placed: {order}")
        return order
    except Exception as e:
        logging.error(f"Error placing market order: {e}")
        return None