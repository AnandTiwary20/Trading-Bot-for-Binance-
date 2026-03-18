from binance.client import Client
from config import API_KEY, API_SECRET

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    return client