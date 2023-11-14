import requests
from datetime import datetime
import smtplib
import time

# Find you locational longitude and latitude
MY_LAT = 11.127693  # Your latitude
MY_LONG = 76.044945  # Your longitude

#Give email and password
EMAIL = "sshuhaib274@gmail.com"
PASSWORD = "App_password"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude >= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
