'''
consumer.py : Routes order details in realtime to the consumer
Info Ingested : order_id,user_id,total_order_value,items
'''
from kafka import KafkaConsumer

consumer = KafkaConsumer('order_publisher', bootstrap_servers='localhost:9092')

print("Gonna start listening")
while True:
    for message in consumer:
        print("Here is a message..")
        print (message)