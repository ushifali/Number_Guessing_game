from kafka import KafkaProducer
import json

# Set up Kafka producer
producer = KafkaProducer(bootstrap_servers=["localhost:9092"])


# Play the game
while True:
    # Get user input for the next guess
    guess = input("Enter your guess (or 'exit' to quit): ")

    if guess == "exit":
        # If the player chooses to exit the game, send a goodbye message and end the game
        break

    # Convert the guess to an integer
    try:
        guess = int(guess)
    except ValueError:
        # If the guess is not a valid integer, continue
        continue

    # Send the player's guess to the consumer
    guess_message = {"type": "guess", "value": guess}
    producer.send("guesses", value=json.dumps(guess_message).encode())
