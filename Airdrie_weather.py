import os as os
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import requests

lat = 51.29
lon = -114.01

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
response = requests.get(url)
data = response.json()

data

print(f'Its {data['current_weather']['temperature']} C in Airdrie today')

today = dt.datetime.today()
last_month = today-dt.timedelta(days = 30)

start_date = last_month.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

data

dw = data['daily']
df = pd.DataFrame(dw)
df.columns = ['date','max temp','min temp'] 

plt.plot(df['date'], df['min temp'], label = 'Min Temp')
plt.plot(df['date'], df['max temp'], label = 'Max Temp')
plt.title('Airdrie min and max temp over last month')
plt.xlabel('Date')
plt.ylabel('Temp in celcius')
plt.legend()
plt.xticks(rotation=45)

df.to_csv('data/airdrie_weather_data.csv')
plt.savefig('airdrie_temps.png')