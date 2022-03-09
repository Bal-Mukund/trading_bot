import websocket,json

crypto_currency = "btcusd"

socket = f"wss://stream.binance.com:9443/ws/{crypto_currency}t@kline_1m"

def on_open(ws):
    print("connection opened")

    
def on_message(ws,message):
    json_message = json.loads(message)
    low  = json_message['l']
    print(low)


def on_close(ws):
    print("connection closed")

ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message,on_close=on_close)

ws.run_forever()