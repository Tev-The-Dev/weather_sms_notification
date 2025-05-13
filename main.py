
import requests

api_call = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0853df0fe250da1fe3dc2fbf53c9ced7"
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
if will_rain:
    print("bring an umbrella")
else:
    print("No rain in sight for the next 12 hours")