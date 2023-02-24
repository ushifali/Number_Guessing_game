from kafka import KafkaProducer
import random

# Set up Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of guesses
num_guesses = 0

# Start the game loop
while True:
    # Get a guess from the user
    guess = input("Enter a number between 1 and 100: ")
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100")
            continue
    except ValueError:
        print("Invalid input, please enter a number")
        continue

    # Send the guess to Kafka
    producer.send('test', str(guess).encode('utf-8'))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations, you guessed the secret number! You needed", num_guesses, "guesses.")
        break
        
    # If the guess is incorrect, give a hint and continue the loop
    if guess < secret_number:
        print("The secret number is greater.")
    else:
        print("The secret number is smaller.")
    num_guesses += 1
