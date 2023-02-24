# Number_Guessing_game
Using Kafka and python

Question:
		Develop a number guessing game. The computer comes up with a random number and you can make guesses. It then tells you if the secret number is greater or smaller. At the end it tells you how many attempts you needed.

Explanation:


The guessing game has two parts: a producer and a consumer. The producer generates a random secret number and then asks the user to guess it. The user inputs their guesses, and the producer sends these guesses as messages to the Kafka topic 'guess'.

The producer generates a random secret number between 1 and 100, and then asks the user to enter a number. The producer sends the user's guess to the 'guess' topic in Kafka, encoded as a UTF-8 string.

The consumer is listening to the 'guess' topic and receives the messages sent by the producer. It checks if the guess is correct, and sends a message to the producer over the 'result' topic indicating if the guess is greater, smaller or equal to the secret number.

The producer receives the message from the consumer over the 'result' topic and displays the response to the user. If the guess is correct, the game ends.

The auto_offset_reset parameter in the consumer instantiation specifies what happens when a consumer first starts reading a topic and there is no previously committed offset for that topic. In this case, we set it to 'earliest', which means that the consumer starts reading from the earliest available offset, i.e. from the beginning of the topic.

Overall, this code demonstrates a simple example of how Kafka can be used to implement a distributed messaging system, where messages are produced by one process and consumed by another.

 
Execution:

1.	Open a terminal window and navigate to the Kafka directory.
Run the following command to start Zookeeper:

bin/zookeeper-server-start.sh config/zookeeper.properties 

2.	Open a new terminal window and navigate to the Kafka directory.
Run the following command to start Kafka:

bin/kafka-server-start.sh config/server.properties 

3.	In a new terminal window, create a topic:

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test 

4.	In another terminal window, start a Kafka producer:

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test 

5.	In another terminal window, start a Kafka consumer:


bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning 

6.	In another terminal run the producer file


python3 producer.py

7.	In another terminal run the consumer file


python3 consumer.py


