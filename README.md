# Kafka Demo Project

This is a simple Kafka project with a producer and consumer using `kafka-python`.

## Prerequisites
- Install kafka
    ```bash
    wget https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz
    tar -xzf kafka_2.13-3.8.0.tgz
    cd kafka_2.13-3.8.0

## Requirements

- Python 3.x
- Apache Kafka installed locally
- `kafka-python` library (see `requirements.txt`)

## Running the Project

1. Start Zookeeper and Kafka:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties

2. Install dependencies:
    pip install -r requirements.txt

3. Run the producer:
    python producer.py

4. Run the consumer:
    python consumer.py
