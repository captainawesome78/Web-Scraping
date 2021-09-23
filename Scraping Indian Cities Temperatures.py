import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get('https://mausam.imd.gov.in/')
print(r.text)

soup  = BeautifulSoup(r.content, 'html.parser')
weathr = soup.find_all('div',class_='capital')

City_name = [items.h3.text for items in weathr]

City_temp = [items.find(class_='val').text for items in weathr]

City_wind = [items.find(class_='wind').text for items in weathr]

print(City_name)
print(City_temp)
print(City_wind)

weather_stuff = pd.DataFrame(

    {'City' : City_name,

    'Temperature' : City_temp,

    'Wind' : City_wind,

    }
)

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
