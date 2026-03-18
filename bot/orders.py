
import logging 

def format_order_response(order):
    if not order:
        return None

    return {
        "orderId": order.get("orderId"),
        "status": order.get("status"),
        "executedQty": order.get("executedQty"),
        "avgPrice": order.get("avgPrice", "N/A")
    }

def place_market_order(client, symbol, side, quantity):
    try: 
        logging.info(f"Placing MARKET order: {symbol} {side} {quantity}")
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
        return format_order_response(order)
    except Exception as e:
        logging.error(f"Error placing market order: {e}")
        return {"error": str(e)}
    
def place_limit_order(client, symbol, side, quantity, price):
    try:
        logging.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")
        
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info(f"Limit order placed: {order}")
        return format_order_response(order)
    
    except Exception as e:
        logging.error(f"Limit order failed: {e}")
        return  {"error": str(e)}