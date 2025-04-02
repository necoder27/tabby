from typing import TypedDict, Literal
import geocoder
import requests


URL = "https://api.open-meteo.com/v1/forecast"


class WeatherCurrent(TypedDict):
    time: str 
    interval: int 
    weather_code: int 
    is_day: Literal[0, 1]
    temperature_2m: float 
    apparent_temperature: float 
    wind_speed_10m: float 
    precipitation: float 
    precipitation_probability: float

class WeatherDaily(TypedDict):
    time: list[str]
    sunrise: list[str]
    sunset: list[str]
    uv_index_max: list[float]

class WeatherResponse(TypedDict):
    latitude: float
    longitude: float
    generationtime_ms: float 
    utc_offset_seconds: int 
    timezone: str 
    timezone_abbreviation: str 
    elevation: float 
    current_units: dict
    current: WeatherCurrent
    daily_units: dict 
    daily: dict 


def get_weather_data() -> WeatherResponse:
    location = geocoder.ip("me")
    
    params = {
        "latitude": location.lat,
        "longitude": location.lng,
        "daily": "sunrise,sunset,uv_index_max",
        "current": "weather_code,is_day,temperature_2m,apparent_temperature,wind_speed_10m,precipitation,precipitation_probability",
        "timezone": "auto",
    }

    response = requests.get(URL, params=params) 
    return response.json()

