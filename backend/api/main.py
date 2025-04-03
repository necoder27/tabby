from fastapi import FastAPI
from backend.os_info import get_macos_version_info, get_uptime_info
from backend.personal_info import get_greeting_based_on_daytime, get_location_from_ip_address
from backend.weather_data import WeatherResponse, get_weather_data
from typing import Any


api = FastAPI()

# Personal Info Endpoints
@api.get("/greeting")
def get_greeting() -> str:
    return get_greeting_based_on_daytime()

@api.get("/location")
def get_location() -> str:
    return get_location_from_ip_address()

# Weather Endpoints
@api.get("/weather")
def get_weather() -> dict[str, Any]:
    return get_weather_data()

# System Info Endpoints 
@api.get("/system/os")
def get_macos_version():
    return get_macos_version_info()

@api.get("/system/uptime")
def get_uptime():
    return get_uptime_info()
