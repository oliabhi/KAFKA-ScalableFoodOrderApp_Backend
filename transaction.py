import json
from kafka import KafkaConsumer, KafkaProducer
from confluent_kafka import avro, avro_serializer
from confluent_kafka.avro.serializer import SerializerError
from google.cloud import bigquery
from google.cloud.bigquery import WriteDisposition

ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"
'''
init GCP PROJECT_ID TO PORT CONFIRMED ORDERS TO BIGQUERY TABLES.
'''
BIGQUERY_PROJECT_ID = "test"
BIGQUERY_DATASET_ID = "orders"
BIGQUERY_TABLE_ID = "CONFIRMED_ORDERS"

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers="localhost:29092"
)
producer = KafkaProducer(bootstrap_servers="")

# Configure the BigQuery client
client = bigquery.Client(project=BIGQUERY_PROJECT_ID)
dataset_ref = client.dataset(BIGQUERY_DATASET_ID)
table_ref = dataset_ref.table(BIGQUERY_TABLE_ID)
table = client.get_table(table_ref)

print("Gonna start listening")

while True:
    for message in consumer:
        print("Ongoing transaction..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)

        user_id = consumed_message["user_id"]
        total_cost = consumed_message["total_cost"]

        # Prepare data for BigQuery
        data = [
            {
                "customer_id": user_id,
                "customer_email": f"{user_id}@gmail.com",
                "total_cost": total_cost
            }
        ]

        # Write data to BigQuery
        errors = client.insert_rows(table, data)

        if errors:
            print(f"Error inserting rows to BigQuery: {errors}")
        else:
            print("Successful transaction..")

        # Forward the message to another Kafka topic if needed
        producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(consumed_message).encode("utf-8"))
