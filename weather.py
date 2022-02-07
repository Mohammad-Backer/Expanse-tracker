import requests
import keys

api_key = keys.API_Key
Base_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Please enter a city name: ")
request_url = f"{Base_url}?appid={api_key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15,2)
    feels_like = round(data['main']['feels_like'] - 273.15,2)
    minimum_temperature = round(data['main']['temp_min'] - 273.15,2)
    maximum_temperature = round(data['main']['temp_max'] - 273.15,2)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
else:
    print("Problem with request!")

print(f"This is the weather report of {city}:")
print(f"The weather is: {weather_description}")
print(f"The temperature is: {temperature} but it feels like {feels_like}")
print(f"The minimum temperature is: {minimum_temperature}")
print(f"The maximum temperature is: {maximum_temperature}")
print(f"The pressure is: {pressure}")
print(f"The humidity is: {humidity}")
print(f"The wind speed is: {wind}")

