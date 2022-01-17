from kafka import KafkaConsumer

consumer = KafkaConsumer('tick')

for msg in consumer:
    print (msg)