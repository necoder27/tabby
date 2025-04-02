import geocoder
import datetime as dt 
from typing import Literal


def get_greeting_based_on_daytime() -> str:
    current_hour = dt.datetime.now().hour

    daytime: Literal["morning", "afternoon", "evening"]
    if 5 <= current_hour < 12:
        daytime = "morning"
    elif 12 <= current_hour < 18:
        daytime = "afternoon"
    else:
        daytime = "evening"

    return f"good {daytime}, laetitia"

def get_location_from_ip_address() -> str: 
    location = geocoder.ip("me")
    return ", ".join([location.city, location.country])

