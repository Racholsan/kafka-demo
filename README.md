# Kafka Demo Project

This is a simple Kafka project with a producer and consumer using `kafka-python`.

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
