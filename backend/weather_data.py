from typing import TypedDict, Literal, Any
import geocoder
import requests
from datetime import datetime as dt 


URL = "https://api.open-meteo.com/v1/forecast"
WMO_WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle: light intensity",
    53: "Drizzle: moderate intensity",
    55: "Drizzle: dense intensity",
    56: "Freezing drizzle: light intensity",
    57: "Freezing drizzle: dense intensity",
    61: "Rain: slight intensity",
    63: "Rain: moderate intensity",
    65: "Rain: heavy intensity",
    66: "Freezing rain: light intensity",
    67: "Freezing rain: heavy intensity",
    71: "Snow fall: slight intensity",
    73: "Snow fall: moderate intensity",
    75: "Snow fall: heavy intensity",
    77: "Snow grains",
    80: "Rain showers: slight",
    81: "Rain showers: moderate",
    82: "Rain showers: violent",
    85: "Snow showers: slight",
    86: "Snow showers: heavy",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}


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
    daily: WeatherDaily 


def filter_weather_data(data: WeatherResponse) -> dict[str, Any]:
    sunrise = data["daily"]["sunrise"][0].split("T")[1]
    sunset = data["daily"]["sunset"][0].split("T")[1]

    sunrise = [sunrise, "am" if (int(sunrise.split(":")[0]) < 12) else "pm"]
    sunset = [sunset, "am" if (int(sunset.split(":")[0]) < 12) else "pm"]

    filtered_weather_data = {
        "weather_code_text": WMO_WEATHER_CODES[data["current"]["weather_code"]],
        "current_temperature": [data["current"]["temperature_2m"], data["current_units"]["temperature_2m"]],
        "apparent_temp": [data["current"]["apparent_temperature"], data["current_units"]["apparent_temperature"]],
        "wind_speed": [data["current"]["wind_speed_10m"], data["current_units"]["wind_speed_10m"]],
        "precipitation_prob": [data["current"]["precipitation_probability"], data["current_units"]["precipitation_probability"]],
        "precipitation": [data["current"]["precipitation"], data["current_units"]["precipitation"]],
        "uv_index_max": data["daily"]["uv_index_max"][0], 
        "sunrise": sunrise, 
        "sunset": sunset,
    }

    return filtered_weather_data 

def get_weather_data() -> dict[str, Any]:
    location = geocoder.ip("me")
    
    params = {
        "latitude": location.lat,
        "longitude": location.lng,
        "daily": "sunrise,sunset,uv_index_max",
        "current": "weather_code,is_day,temperature_2m,apparent_temperature,wind_speed_10m,precipitation,precipitation_probability",
        "timezone": "auto",
    }

    response = requests.get(URL, params=params)
    filtered_data = filter_weather_data(response.json())

    return filtered_data 

