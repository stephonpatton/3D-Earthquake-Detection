import requests

hourly_api = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(hourly_api)
rep_json = response.json()
print(response.json())

for i in range(len(rep_json)):
    features = rep_json['features'][i]['properties']['place'] # Get location of earthquake from today
    print(features)