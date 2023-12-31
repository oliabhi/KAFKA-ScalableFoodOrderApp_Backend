# Kafka Based Scalable Food Order App Backend

This repository contains Python scripts implementing a simple real-time order processing system using Kafka for message queuing. The system comprises three main components:

1. **Order Backend (`order_backend.py`):**
   - Generates mock order data with details such as `order_id`, `user_id`, `total_order_value`, and `items`.
   - Sends the generated order data to the Kafka topic "order_publisher" every 10 seconds.

2. **Consumer (`consumer.py`):**
   - Listens to the Kafka topic "order_publisher."
   - Consumes incoming order data in real-time and prints the messages.

3. **Transactions (`transactions.py`):**
   - Listens to the Kafka topic "order_details."
   - Processes incoming order details, extracts relevant information (`user_id`, `total_cost`), and simulates a transaction.
   - Sends a confirmation message with details such as `customer_id`, `customer_email`, and `total_cost` to the "order_confirmed" Kafka topic.

## Prerequisites

- Python 3.x
- Kafka (Ensure Kafka server is running locally with default configurations)

## Setup

1. Install the required Python packages:
   ```bash
   pip install kafka-python


#### Ensure that the Kafka server is running locally on the default ports.


#### Usage

- Run the order_backend.py script to start generating and sending mock orders to the "order_publisher" Kafka topic:
    python order_backend.py

-  Run the consumer.py script to listen to incoming orders on the "order_publisher" Kafka topic:
    python consumer.py

- Run the transactions.py script to process orders, simulate transactions, and send confirmation messages to the "order_confirmed" Kafka topic:
    python transactions.py

##### Notes

- Adjust the Kafka bootstrap server configurations in the scripts if your Kafka server is running on a different host or port.

- The scripts use the kafka-python library for interacting with Kafka. Ensure that the library is installed in your Python environment.

- Mock order data is generated and processed to demonstrate the flow of information through Kafka topics in real-time.


Feel free to copy and paste this Markdown code into your README.md file.
