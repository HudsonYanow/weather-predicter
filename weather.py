# import requests_cache
import pandas as pd
import requests
import datetime

# Function to extract the day from the date
def extractDay(date):
    """Extract the day from the date"""
    year=date.split("-")[0]
    month=date.split("-")[1]
    day=date.split("-")[2]
    """Returns a string of the day of the week"""
    return datetime.datetime(int(year),int(month),int(day)).strftime("%A")

# Function to validate the latitude and longitude
def validateFloats(lat,lon):
    """Validate the latitude and longitude"""
    ok=False
    while not ok:
        try:
            float(lat)
            float(lon)
            ok=True
        except:
            print("please enter a valid input")
            lat=input("What is the latitude of your location: ")
            lon=input("What is the longitude of your location: ")
            
    return lat,lon

# Function to get the weather forecast from the API
def getWeatherForecast(lat,lon):
    """Get the weather forecast from the API"""
    # Install the cache for the requests to the API to avoid making the same request multiple times
    # requests_cache.install_cache('weather_cache', backend='sqlite', expire_after=3600)
    # Get the weather forecast from the API
    url = "https://api.open-meteo.com/v1/forecast"
    # Set the parameters for the request
    params = {
        "latitude": lat,
        "longitude": lon,
        "weekly": "temperature_2m",
        "forecast_days": 7,
        "temperature_unit": "fahrenheit",
        "daily":"weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset"
    }
    # Make the request
    response = requests.get(url, params=params)
    data=response.json()
    return data

# Main code

# Welcome message
print("Welcome to the Weather Forecast App")
print("""What is the latidue and longitude of your location for example\n
London:lat: 51.5085 lon: -0.1257\n
New York: lat: 40.7143 lon: -74.006\n
Paris: lat: 48.8534 lon: 2.3488\n
Tokyo: lat: 35.6895 lon: 139.6917\n
Sydney: lat: -33.8678 lon: 151.2073\n""")
# Get the latitude and longitude of the location from the user input
lat=input("What is the latitude of your location: ")
lon=input("What is the longitude of your location: ")
# Validate the latitude and longitude
validateFloats(lat,lon)

try:    
    # Get the weather forecast from the API
    data=getWeatherForecast(lat,lon)
# Print the error message if the API is down
except Exception as e:
    print("The following error occurred: ", e)

active=True
while active==True:

    # Ask the user what they want to do
    inp=input("""Do you want to:\n
1)Get the weather forecast for the next day.\n
2)Get the weather forecast for the upcoming week.\n
3)Change coordinates.\n
4)Exit the program\n""")
    
    if inp=="1":
        # Get the weather code, max temp, min temp, sunrise and sunset for the next day
        weahtherCode=data["daily"]["weather_code"][1]
        maxTemp=data["daily"]["temperature_2m_max"][1]
        minTemp=data["daily"]["temperature_2m_min"][1]
        sunrise=data["daily"]["sunrise"][1].split("T")[1]
        sunset=data["daily"]["sunset"][1].split("T")[1]
        print(f"the weather code is {weahtherCode}")
        print(f"the max temp is {maxTemp}")
        print(f"the min temp is {minTemp}")
        print(f"the sun will rise at {sunrise} and set at {sunset}")
    elif inp=="2":
        # Get the weather code, max temp, min temp, sunrise and sunset for the upcoming week
        day0=extractDay(data["daily"]["time"][0])
        day1=extractDay(data["daily"]["time"][1])
        day2=extractDay(data["daily"]["time"][2])
        day3=extractDay(data["daily"]["time"][3])
        day4=extractDay(data["daily"]["time"][4])
        day5=extractDay(data["daily"]["time"][5])
        day6=extractDay(data["daily"]["time"][6])
        maxTemp0=data["daily"]["temperature_2m_max"][0]
        minTemp0=data["daily"]["temperature_2m_min"][0]
        maxTemp1=data["daily"]["temperature_2m_max"][1]
        minTemp1=data["daily"]["temperature_2m_min"][1]
        maxTemp2=data["daily"]["temperature_2m_max"][2]
        minTemp2=data["daily"]["temperature_2m_min"][2]
        maxTemp3=data["daily"]["temperature_2m_max"][3]
        minTemp3=data["daily"]["temperature_2m_min"][3]
        maxTemp4=data["daily"]["temperature_2m_max"][4]
        minTemp4=data["daily"]["temperature_2m_min"][4]
        maxTemp5=data["daily"]["temperature_2m_max"][5]
        minTemp5=data["daily"]["temperature_2m_min"][5]
        maxTemp6=data["daily"]["temperature_2m_max"][6]
        minTemp6=data["daily"]["temperature_2m_min"][6]
        print(f"the max temp on {day0} is {maxTemp0} and the min is {minTemp0}")
        print(f"the max temp on {day1} is {maxTemp1} and the min is {minTemp1}")
        print(f"the max temp on {day2} is {maxTemp2} and the min is {minTemp2}")
        print(f"the max temp on {day3} is {maxTemp3} and the min is {minTemp3}")
        print(f"the max temp on {day4} is {maxTemp4} and the min is {minTemp4}")
        print(f"the max temp on {day5} is {maxTemp5} and the min is {minTemp5}")
        print(f"the max temp on {day6} is {maxTemp6} and the min is {minTemp6}")
    elif inp=="3":
        # Update the latitude and longitude of the user location
        lat=input("what is the latitude of your location")
        lon=input("what is the longitude of your location")
        # Validate the latitude and longitude
        validateFloats(lat,lon)
        # Update the weather forecast with the new latitude and longitude
        data=getWeatherForecast(lat,lon)
    elif inp=="4":
        # Exit the program
        active=False
    else:
        # Print the error message if the input is not valid
        print("please enter a valid input")
        continue