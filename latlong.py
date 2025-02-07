import json
import math
from geopy.distance import geodesic

# Load known stations data from data.json
with open('data.json', 'r') as f:
    data_json = json.load(f)

# Load sub-district HQ data from AP_sub_dist_hq.geojson
with open('AP_sub_dist_hq.geojson', 'r') as f:
    geojson_data = json.load(f)

# Function to calculate distance between two points (lat, lon)
def calculate_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon1)).kilometers

# Function to interpolate fluoride values based on inverse distance weighting
def interpolate_fluoride(nearest_stations):
    weighted_sum = 0
    total_weight = 0
    for station in nearest_stations:
        dist = station['distance']
        if dist == 0:  # Prevent division by zero
            return station['fluoride']
        weight = 1 / dist  # Inverse distance weighting
        weighted_sum += station['fluoride'] * weight
        total_weight += weight
    return weighted_sum / total_weight

# Prepare list of known stations with fluoride data
known_stations = [
    {
        "latitude": station['Latitude'],
        "longitude": station['Longitude'],
        "fluoride": station['Fluoride']
    }
    for station in data_json['stations']
]

# For each point in AP_sub_dist_hq.geojson, check if it's missing in data.json
for feature in geojson_data['features']:
    latitude = feature['geometry']['coordinates'][1]
    longitude = feature['geometry']['coordinates'][0]
    
    # Check if this location already exists in data.json
    already_known = any(
        station['Latitude'] == latitude and station['Longitude'] == longitude
        for station in data_json['stations']
    )
    
    if not already_known:
        # Calculate distance to all known stations
        distances = []
        for station in known_stations:
            dist = calculate_distance(latitude, longitude, station['latitude'], station['longitude'])
            distances.append({
                "station": station,
                "distance": dist,
                "fluoride": station['fluoride']
            })
        
        # Sort distances to find nearest stations
        distances.sort(key=lambda x: x['distance'])
        
        # Use interpolation if more than one station is nearby
        nearest_stations = distances[:3]  # Consider up to 3 nearest stations
        predicted_fluoride = interpolate_fluoride(nearest_stations)
        
        # Append predicted fluoride value to data.json with updated station name and district
        data_json['stations'].append({
            "Station": feature['properties']['LOC_NAME'],  # Update station name
            "Latitude": latitude,
            "Longitude": longitude,
            "District": feature['properties']['dtname'],  # Update district name
            "Fluoride": predicted_fluoride
        })

# Save updated data.json
with open('data_updated.json', 'w') as f:
    json.dump(data_json, f, indent=4)

print("Predicted fluoride values have been added to data.json with updated station and district names.")
