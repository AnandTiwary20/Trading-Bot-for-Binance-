from binance.client import Client
from config import API_KEY, API_SECRET
from logging_config import logging

def get_client():
    try:
        client = Client(API_KEY, API_SECRET)
        client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logging.info("Binance client initialized")
        return client

    except Exception as e:
        logging.error(f"Failed to initialize client: {e}")
        raise