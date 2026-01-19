import requests

lat = 51.2917
lon = -114.01

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

print(data)

data.keys()

data['current_weather']['temperature']

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data['current_weather']['temperature']


paris_temp = get_weather(48.8566, 2.3522)
dubai_temp = get_weather(25.2048, 55.2708)

print(f'The temperature in paris is {paris_temp}')
print(f'the temp ins dubai is {dubai_temp}')

