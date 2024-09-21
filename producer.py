from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_messages(topic, num_messages=10):
    for i in range(num_messages):
        message = {'key': i, 'value': f'message {i}'}
        producer.send(topic, message)
        print(f'Sent: {message}')
        time.sleep(1)  # Simulating delay between messages

if __name__ == "__main__":
    send_messages('test-topic')
    producer.close()
