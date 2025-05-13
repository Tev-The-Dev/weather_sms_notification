import os
from dotenv import load_dotenv

load_dotenv()

import requests

from twilio.rest import Client
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")


api_call = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("WEATHER_API_KEY")

my_phone = os.getenv("MY_PHONE")
send_phone = os.getenv("WHATSAPP_PHONE")

long = -97.082685
lat = 32.837287
parameters = {
    "lat":lat,
    "lon":long,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(api_call, params=parameters)
response.raise_for_status()

data=response.json()

will_rain = False
for entry in data["list"]: #loops through every item in the list
    weather_info = entry["weather"][0] #gets the weather identifier of every list item
    if weather_info["id"] < 700:
        will_rain=True
    print(weather_info["id"],"-",weather_info["description"]) #prints the id and description of the weather item
#print(data["list"][0]["weather"][0]["id"], data["list"][0]["weather"][0]["description"])
client = Client(account_sid, auth_token)
if will_rain:
    message = client.messages.create(from_=send_phone,body='Bring and umbrella. Chance of rain high.',to=my_phone)
    print(message.status)
else:
    message = client.messages.create(from_=send_phone,body= 'No need to bring an umbrella. Chance of rain low',to = my_phone)
    print(message.status)