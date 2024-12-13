import json
import websocket
from kafka import KafkaProducer

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'binance-trades'

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Binance Combined WebSocket for BTC/USDT and ETH/USDT
socket = 'wss://stream.binance.com:9443/stream?streams=btcusdt@trade/ethusdt@trade'

def on_message(ws, message):
    # The combined stream returns data in the "data" field
    msg = json.loads(message)

    # Extract the "data" portion which contains the trade info
    trade_data = msg.get('data', {})

    # Publish the raw trade data to Kafka
    producer.send(KAFKA_TOPIC, value=trade_data)  
    print(f"Published: {json.dumps(trade_data)}")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

# WebSocket App
ws = websocket.WebSocketApp(socket,
                             on_open=on_open,
                             on_message=on_message,
                             on_error=on_error,
                             on_close=on_close)

ws.run_forever()
