from kafka import KafkaConsumer

consumer = KafkaConsumer('order_publisher', bootstrap_servers='localhost:9092')

print("Gonna start listening")
while True:
    for message in consumer:
        print("Here is a message..")
        print (message)