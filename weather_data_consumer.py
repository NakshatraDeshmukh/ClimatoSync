from confluent_kafka import Consumer, KafkaException
import psycopg2
import json

# Kafka Consumer configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'weather_consumer_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(kafka_config)
consumer.subscribe(['weather-data-topic'])

# PostgreSQL database connection
db_connection = psycopg2.connect(
    host="localhost",
    database="weather_data",
    user="postgres",
    password="1121"
)
cursor = db_connection.cursor()

# Function to insert weather data into PostgreSQL
def insert_weather_data(data):
    try:
        query = """
            INSERT INTO weather (timestamp, temperature, humidity, condition, city)
            VALUES (%s, %s, %s, %s, %s);
        """
        values = (
            data['timestamp'],
            data['temperature'],
            data['humidity'],
            data['condition'],
            data['city']
        )
        cursor.execute(query, values)
        db_connection.commit()
    except Exception as e:
        print(f"Error inserting data into PostgreSQL: {e}")
        db_connection.rollback()

# Consumer loop
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        weather_data = json.loads(msg.value().decode('utf-8'))
        insert_weather_data(weather_data)
        print(f"Data successfully inserted: {weather_data}")
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()
    cursor.close()
    db_connection.close()
