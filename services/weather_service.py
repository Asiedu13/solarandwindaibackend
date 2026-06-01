import requests
# imports the requests library to make queries to weather APIs

def fetch_weather_data(lat, lon ):
    # Function fetches weather data for a specified loaction using the latitude and longitude
    url = "https://api.open-meteo.com/v1/forecast"
    # door for current weather data.

    # create a dictionary of parameters of key value pairs.
    parameters = {
        "latitude": lat,
        "longitude": lon,
        
        "hourly": ( # hourly values for these variables
            "temperature_2m," # temperature at 2 meters above the ground.
            "cloud_cover," # percentage the sky is covered by clouds.
            "shortwave_radiation" # sunlight reaching the earth's surface.
        ),
        "forecast_days": 1,
        "timezone": "auto"

    }

    response = requests.get(url, params=parameters, timeout=10) # max waiting time is 11 seconds.
    response.raise_for_status() # rasies an exceptions if the request was unsucessful.

    data = response.json()

    hourly = data["hourly"]

    radiation_values = hourly["shortwave_radiation"]
# gets sunlight values for each hour

    avg_radiation = sum(radiation_values)/ len(radiation_values)

    return {
        "temperature": sum(hourly["temperature_2m"])/len(hourly['temperature_2m']),
        "cloud_cover": sum(hourly["cloud_cover"])/ len(hourly["cloud_cover"]),
        "shortwave_radiation": avg_radiation
    }

# average cloudiness represents the days sunlight conditions

# NOTE: Taking the average of the houly values gives
# a more clear representation of the day's weather conditions
