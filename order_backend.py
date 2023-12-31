import json
import time

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_publisher"
ORDER_LIMIT= 10

producer = KafkaProducer(bootstrap_servers="localhost:9092")

print("Generating Order ID")
print("Generating orders every 10 seconds")

# time.sleep(10)

for i in range(0, ORDER_LIMIT):
    order_data= {
        "order_id": i,
        "user_id":f"user_{i}",
        "total_order_value":i*100,
        "items":"bbq-steak"
    }

    producer.send(ORDER_KAFKA_TOPIC, json.dumps(order_data).encode("utf-8"))
    print(f"order_id : {i} sent")
    time.sleep(10)