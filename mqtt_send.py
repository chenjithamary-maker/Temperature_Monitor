import paho.mqtt.client as mqtt
import time
from weather_fetch import get_weather

AIO_USERNAME = "Chenjitha"
AIO_KEY = "aio_ZBGo58FhJJnjZ501nssafiVxdE9S"

broker = "io.adafruit.com"
port = 1883

client = mqtt.Client()
client.username_pw_set(AIO_USERNAME, AIO_KEY)
client.connect(broker, port, 60)

while True:
    temp, hum = get_weather()

    print("Sending:", temp, hum)

    client.publish(f"{AIO_USERNAME}/feeds/temperature", temp)
    client.publish(f"{AIO_USERNAME}/feeds/humidity", hum)

    # wait before next update
    time.sleep(10)   # or 3600 for hourly