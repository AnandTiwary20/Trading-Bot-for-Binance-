from client import get_client
from logger import setup_logger
from orders import place_market_order, place_limit_order

def main():
    setup_logger()