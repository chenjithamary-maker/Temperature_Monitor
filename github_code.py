import requests
import smtplib
import time

# Adafruit IO details
AIO_USERNAME = "Chenjitha"
AIO_KEY = "aio_ZBGo58FhJJnjZ501nssafiVxdE9S"
FEED_NAME = "temperature"

# Email details
sender_email = "chenjithamary@gmail.com"
password = "juor mvth gqww mpgm"

receivers = ["saljin9a@gmail.com", "codewithchen@gmail.com"]

# API URL
url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME}/data/last"

def get_temperature():
    headers = {"X-AIO-Key": AIO_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return float(data['value'])

def send_email(temp):
    subject = " Temperature Alert"
    body = f"Temperature exceeded! Current value: {temp}C"

    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    for email in receivers:
        server.sendmail(sender_email, email, message)

    server.quit()

# Continuous monitoring
while True:
    try:
        
        temp = get_temperature()
        print("Current Temp:", temp)
        print("DEBUG -> Temp value is:", temp, "| Type:", type(temp))

        if temp > 20:
            print("Condition met. Sending email...")
            send_email(temp)
            time.sleep(300)  # wait 5 min to avoid spam
        else:
            time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(10)
