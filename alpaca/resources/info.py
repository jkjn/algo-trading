import alpaca_trade_api as tradeapi
import os

def handler():
  api = tradeapi.REST(
    base_url='https://paper-api.alpaca.markets'
  )
  account = api.get_account()
  api.list_positions()

  print(account)

if __name__ == "__main__":
    handler()