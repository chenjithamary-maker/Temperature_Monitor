from flask import Flask
import threading
import time
import requests
import smtplib
import os

app = Flask(__name__)

AIO_USERNAME = os.getenv("Chenjitha")
AIO_KEY = os.getenv("aio_qECL32DbrUzEiDGQhM8oHAidSRht")
FEED_NAME = "temperature"

sender_email = os.getenv("chenjithamary@gmail.com")
password = os.getenv("juor mvth gqww mpgm")

receivers = ["saljin9a@gmail.com", "codewithchen@gmail.com"]

url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME}/data/last"

def get_temperature():
    headers = {"X-AIO-Key": AIO_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return float(data['value'])

def send_email(temp):
    subject = "Temperature Alert"
    body = f"Temperature exceeded! Current value: {temp}C"
    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    for email in receivers:
        server.sendmail(sender_email, email, message)

    server.quit()

def monitor():
    while True:
        try:
            temp = get_temperature()
            print("Temp:", temp)

            if temp > 0:
                send_email(temp)
                time.sleep(300)
            else:
                time.sleep(10)

        except Exception as e:
            print("Error:", e)
            time.sleep(10)

@app.route("/")
def home():
    return "Temperature Monitoring Running!"

if __name__ == "__main__":
    threading.Thread(target=monitor).start()
    app.run(host="0.0.0.0", port=10000)
