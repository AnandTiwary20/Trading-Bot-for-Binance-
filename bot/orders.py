
import logging 

def place_market_order(client, symbol, side, quantity):
    try: 
        order =client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        
        )