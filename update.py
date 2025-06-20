import requests
from datetime import datetime
import pytz
import os



API_KEY = os.environ['WEATHER_API_KEY']
CITY = "Taif,SA"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=en"

now = datetime.now(pytz.timezone('Asia/Riyadh'))
date_str = now.strftime('%Y-%m-%d %H:%M:%S')
res = requests.get(URL)
data = res.json()

weather = data['weather'][0]['description'].capitalize()
temp = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']

# Write to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🌤️ Today's Weather in Taif, Saudi Arabia\n\n")
    f.write(f"**📅 Date:** {date_str}\n\n")
    f.write(f"- **Condition:** {weather}\n")
    f.write(f"- **Temperature:** {temp}°C\n")
    f.write(f"- **Humidity:** {humidity}%\n")
    f.write(f"- **Wind Speed:** {wind_speed} m/s\n")
