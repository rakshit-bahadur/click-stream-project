from kafka import KafkaConsumer
import json

class KafkaConsumer:
    def __init__(self, topic, bootstrap_servers):
        self.consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

    def consume(self):
        return self.consumer

    def process_message(self, message):
        data = json.loads(message.value)
        return data
