import requests
import time

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=11.0055&longitude=76.9661&minutely_15=temperature_2m,relative_humidity_2m&forecast_days=1"
    
    try:
        response = requests.get(url)
        data = response.json()

        # Extract minutely data correctly
        temp_2m = data['minutely_15']['temperature_2m'][0]
        humidity = data['minutely_15']['relative_humidity_2m'][0]

        return temp_2m, humidity

    except Exception as e:
        print("Error fetching weather data:", e)
        return None, None


if __name__ == "__main__":
    while True:
        temp, hum = get_weather()

        if temp is not None and hum is not None:
            print("\n--- Live Weather Data ---")
            print("Temperature:", temp, "°C")
            print("Humidity:", hum, "%")
        else:
            print("Failed to fetch data... retrying")

        # Fetch every 3600 seconds
        time.sleep(10)