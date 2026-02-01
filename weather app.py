import requests

# Your OpenWeather API key
API_KEY = "7f4dfa07c7f10eca09a13b20528d8cd3"

# Take city name from user
city = input("Enter city name: ")

# Build API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)
data = response.json()

# Check if request was successful
if response.status_code == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print("\n----------------------------")
    print(f"🌍 Weather in {city}")
    print("----------------------------")
    print(f"🌡 Temperature : {temp}°C")
    print(f"☁ Condition    : {weather}")
    print(f"💧 Humidity    : {humidity}%")
    print(f"💨 Wind Speed  : {wind} m/s")
    print("----------------------------")

else:
    print("❌ City not found or API error")
