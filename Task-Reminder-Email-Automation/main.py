import requests
from twilio.rest import Client

# OpenWeatherMap API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "8bbf1252c9045423358fa739da0981e6"

# Location details
weather_params = {
    "lat": 10.114700,
    "lon": 76.477798,
    "appid": api_key,
}

# Fetch weather data
response = requests.get(OWM_Endpoint, params=weather_params)
data = response.json()

# Extract weather details
details1 = data["weather"][0]
details2 = data["main"]
details3 = data["wind"]

description = details1["description"]
mainly = details1["main"]
temperature = int(details2["temp"]) - 273.15  # Convert from Kelvin to Celsius
wind = details3["speed"]

# Twilio account SID and Auth Token
account_sid = 'Your ID'
auth_token = 'Your unique token'
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body=f"Temp: {temperature:.2f}°C\nWindspeed: {wind} m/s\nMain: {mainly}\nDesc: {description}",
    from_="Twilio phone number",
    to="Verified phone number",  
)
