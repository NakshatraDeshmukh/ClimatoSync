from confluent_kafka import Producer
import requests
import json
import time
from datetime import datetime, timezone

# Kafka producer configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'weather_data_producer'
}
producer = Producer(kafka_config)

# OpenWeatherMap API Configuration
api_key = "b2da6fc8252cc95463ce0aad3b6ce3fb"
city = "Pune,in"
weather_data_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Delivery report callback
def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Record sent to {msg.topic()} partition [{msg.partition()}] @ offset {msg.offset()}")

# Function to fetch and send weather data
def fetch_and_send_weather_data():
    try:
        response = requests.get(weather_data_url)
        response.raise_for_status()

        weather_data = response.json()
        weather_info = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'condition': weather_data['weather'][0]['description'],
            'city': city
        }
        producer.produce(
            'weather-data-topic',
            json.dumps(weather_info),
            callback=delivery_report
        )
        producer.flush()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        while True:
            fetch_and_send_weather_data()
            time.sleep(600)  # Sleep for 10 minutes
    except KeyboardInterrupt:
        print("Shutting down producer gracefully...")
    finally:
        producer.flush()  # Close the producer to release resources
        print("Producer closed.")