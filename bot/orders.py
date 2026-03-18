
import logging 

def place_market_order(client, symbol, side, quantity):
    try: 
        order =client.futures_create_order(  
                                                      #may need to failure if the input is not validated
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
                                                #  Mapping internal function inputs  into external API contract
                                                 #  This is called DTO mapping (Data Transfer Object)

        )
        logging.info(f"Market order placed: {order}") 
        return order
    except Exception as e:
        logging.error(f"Error placing market order: {e}")
        return None
    
def place_limit_order(client, symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info(f"Limit order placed: {order}")
        return order
    except Exception as e:
        logging.error(f"Error placing limit order: {e}")
        return None