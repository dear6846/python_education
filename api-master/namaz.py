import requests
import json

contry='tashkent'
url = f"https://dailyprayer.abdulrcs.repl.co/api/{contry}"
response = requests.get(url)
data = response.json()
print(data['city'])
print(data['date'])
for namaz in data["today"]:
  print(namaz + ": " + data["today"][namaz])