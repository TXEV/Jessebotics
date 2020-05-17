import requests
import json

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Surrey,CA&appid=b76748d36e933cc435b3f697c5db3ff9")
data = json.loads(r.text)
current_weather = data["weather"][0]["main"]

print(current_weather)