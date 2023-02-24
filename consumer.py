from kafka import KafkaConsumer

# Create Kafka consumer with topic 'test' and connect to Kafka broker at localhost:9092
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], auto_offset_reset='latest')

# # Continuously listen for messages on the 'test' topic
for message in consumer:
    # Decode the message value (which is in bytes) to a string and convert to integer
    value = message.value.decode('utf-8')

    # Print the received guess
    if value.isdigit():
        guess = int(value)
        print("Received guess:", guess)
    else:
        print("Invalid guess received:", value)
