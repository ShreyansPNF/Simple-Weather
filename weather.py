import requests

API_KEY = "a7b2d07d6407c8fc103d308c12b52c76"  # Replace with your actual key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'  # 'imperial' for Fahrenheit
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    main = data["main"]
    weather = data['weather'][0]['description']
    temp = main['temp']
    humidity = main['humidity']
    wind_speed = data['wind']['speed']
    feel_like = main['feels_like']
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feel_like}°C")
else:
    print("City not found. Please try again.")
    
print ("Weather data retrieved successfully.")
if humidity < 30:
    print("It's dry outside, consider using a humidifier.")
elif [humidity > 70]:
    print("It's quite humid outside, stay hydrated.")

if wind_speed > 10:
    print("It's windy outside, hold onto your hat!")
else:
    print("The wind is calm, enjoy your day!")

if temp < 0:
    print("It's freezing outside, bundle up!")      

elif temp > 30:
    print("It's hot outside, stay cool!")
else:
    print("The weather is pleasant, enjoy your day!")

if feel_like < 0:
    print("It feels freezing outside, bundle up!")
elif feel_like > 30:
    print("It feels hot outside, stay cool!")
else:
    print("The weather feels pleasant, enjoy your day!")
print("Weather conditions checked successfully.")
print("Weather script executed successfully.")





