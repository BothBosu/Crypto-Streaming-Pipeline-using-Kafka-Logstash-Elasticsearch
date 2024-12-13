# Crypto-Streaming-Pipeline-using-Kafka-Logstash-Elasticsearch

This project is a part of the Streaming Data Pipeline and Data Visualization project for ICCS361 at Mahidol University International College. This project demonstrates a real-time data streaming pipeline using trading data from Binance WebSocket API for the BTC/USDT and ETH/USDT trading pairs. The pipeline ingests, processes, and visualizes data using a stack of modern tools including Kafka, Logstash, Elasticsearch, and Kibana, all containerized with Docker.

---

## Data Flow Pipeline

The project’s architecture consists of the following steps:

1. **Data Source:** Trading data is fetched from the Binance WebSocket API, which includes details such as event time, symbol, trade ID, price, quantity, and more.

2. **Buffering:** Kafka serves as a buffering layer, ensuring scalability and fault tolerance for the data stream.

3. **Data Aggregation & Processing:** Logstash processes and transforms the Kafka data to make it suitable for indexing into Elasticsearch.

4. **Indexing & Visualization:** Processed data is stored in Elasticsearch and visualized on a Kibana dashboard to enable real-time insights.

![Data Pipeline](https://github.com/user-attachments/assets/a8285119-7c6e-491e-9fda-4b8d334156a9)
![image](https://github.com/user-attachments/assets/fb35622d-ff06-4a70-8fb9-ecd03ea32824)

---

## Data Format

Data from the Binance WebSocket API is structured as follows:

- **e:** Event type
- **E:** Event time (in milliseconds since Unix epoch)
- **s:** Symbol (e.g., BTCUSDT, ETHUSDT)
- **t:** Trade ID
- **p:** Price
- **q:** Quantity
- **T:** Trade time (in milliseconds since Unix epoch)
- **m:** Buyer market maker flag
- **M:** Ignore (always true and can be ignored)
  
---

## Setup Instructions

### Prerequisites
- Docker and Docker Compose installed.
- Python 3.9+ installed.
- Access to a Binance account to retrieve WebSocket API data.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/BothBosu/Crypto-Streaming-Pipeline-using-Kafka-Logstash-Elasticsearch.git
   cd .\Crypto-Streaming-Pipeline-using-Kafka-Logstash-Elasticsearch\

2. **Run Docker Containers:**
     ```bash
    docker-compose up
     ```

3. **Start the Producers:**
   ```bash
   python producer/kafka_crypto_producer.py
   ```

4. **Access Kibana Dashboard:** Open Kibana at http://localhost:5601 
