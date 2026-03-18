# Trading Bot (Binance Futures Testnet)

## Features

* Market and Limit order support
* CLI-based input
* Logging and error handling
* Modular architecture

## Setup

pip install -r requirements.txt

## Run Example

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

## Notes

* Uses Binance Futures Testnet
* If API fails, mock response is returned for demonstration
