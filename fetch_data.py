import websocket,json
# from forex_python.converter import CurrencyRates
# from pymongo import MongoClient
# import numpy as np
# import talib

#
# RSI_INTERVAL = 14
# RSI_OVERBOUGHT = 70
# RSI_OVERSOLD = 30

# client = MongoClient()
# db = client["closes"]
# colllection = db["bit-closes"]

# closes = []
# in_position = False

crypto_currency = "btcusd"

socket = f"wss://stream.binance.com:9443/ws/{crypto_currency}t@kline_1m"

# currency1 = "USD"
# currency2 = "INR"

def on_open(ws):
    print("connection opened")


def on_message(ws,message):
    # global all_closes
    # global close
    json_message = json.loads(message)
    print(json_message)
    # candle_stick = json_message["k"]
    # is_close = candle_stick["x"]
    # close = candle_stick["c"]
    # print(json_message)

    # if is_close:
    #     # c = CurrencyRates()
    #     # change_rates = c.get_rate(currency1, currency2)
    #     # indian_price= change_rates * float(close)
    #
    #     closes.append(float(close))
    #     print(len(closes))
    #
    #     if len(closes) > RSI_INTERVAL:
    #         np_closes= np.array(closes)
    #         rsi = talib.RSI(np_closes,RSI_INTERVAL)
    #         last_rsi = rsi[-1]
    #         print(last_rsi)
    #
    #
    #         if last_rsi >= RSI_OVERBOUGHT:
    #             if in_position:
    #                 print("sell! sell! sell!")
    #
    #             else:
    #                 print("overbought!  but we don't own any")
    #
    #         if last_rsi <= RSI_OVERSOLD :
    #             if in_position:
    #                 print("oversold! but we already own it")
    #             else:
    #                 print("buy! buy! buy!")
    #
    #
    #     # dic = {"close":indian_price}
    #     #colllection.insert_one(dic)


def on_close(ws):

    print("connection closed")


ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message,on_close=on_close)

ws.run_forever()

