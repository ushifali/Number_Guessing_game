from kafka import KafkaConsumer
import json
import random

# Set up Kafka consumer for guesses and messages
guess_consumer = KafkaConsumer("guesses", bootstrap_servers=["localhost:9092"])

# Generate a random number for the player to guess
secret_number = random.randint(1, 100)

# Initialize the number of guesses made
num_guesses = 0


# Listen for guesses from the producer and respond with hints accordingly
for guess in guess_consumer:
    guess_data = json.loads(guess.value.decode())
    guess_value = guess_data["value"]

    # Increment the number of guesses made
    num_guesses += 1

    if guess_value == secret_number:
        # If the player guesses correctly, print a congratulatory message and end the game
        success_message = f"Congratulations, you guessed the secret number {secret_number} in {num_guesses} guesses!"
        print(success_message)
        break
    elif guess_value < 1 or guess_value > 100:
        # If the player's guess is out of range, send an error message
        error_message = {
            "type": "error",
            "text": "Invalid guess. Please enter a number between 1 and 100.",
        }
        print(error_message["text"])
    elif num_guesses == 10:
        # If the player has used up all their guesses, print a failure message and end the game
        failure_message = f"Sorry, you did not guess the secret number {secret_number} in 10 tries. Better luck next time!"
        print(failure_message)
        break
    elif guess_value < secret_number:
        # If the player's guess is too low, print a hint message
        print("Your guess is too low. Guess again.")
    elif guess_value > secret_number:
        # If the player's guess is too high, print a hint message
        print("Your guess is too high. Guess again.")
        
    
