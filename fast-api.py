import requests
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

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

today = dt.date.today()
week_ago = today - dt.timedelta(days=7)
print(f'Today is {today} and a week ago it was {week_ago}')

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

daily_temp = data['daily']

df = pd.DataFrame(daily_temp)
df.columns = ['time','max temp','min temp']

df

plt.plot(df['time'], df['max temp'], label='Max Temp')
plt.plot(df['time'], df['min temp'], label='Min Temp')
plt.title('Paris Min and Max temperatures over the last week')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.xticks(rotation=45)
plt.savefig('paris_temps.png')
plt.show()