import requests

import db_manager

# hourly_api = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
hourly_api = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2022-01-01&endtime=2022-02-01"
response = requests.get(hourly_api)
rep_json = response.json()
print(rep_json)
print(len(response.json()))
db_manager.open_connection()
hourly_quakes = rep_json['metadata']['count']
print("Hourly Quakes: ", hourly_quakes )

for i in range(hourly_quakes):
    properties = rep_json['features'][i]['properties']
    location = rep_json['features'][i]['geometry']['coordinates'] # long, lat, depth
    print(location)
    mag = properties['mag']
    # print(mag)
    city = 21  # Todo: Extract city from response
    time = properties['time']
    updated = properties['updated']
    detail = properties['detail']
    longitude = location[0]
    latitude = location[1]
    depth = location[2]
    print(longitude, latitude, depth)
    country = 'US'  # TODO: Extract country from response
    id = rep_json['features'][i]['id']
    # db_manager.insert_mag(mag)
    db_manager.insert_quake(mag, city, time, updated, detail, longitude, latitude, depth, country, id)
    # features = rep_json['features'][i]['properties']['place'] # Get location of earthquake from today

    # print(mag, time, updated, detail)

# db_manager.select_rows()
db_manager.close_connection()
