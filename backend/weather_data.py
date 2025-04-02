from typing import TypedDict, Literal, Any
import geocoder
import requests


URL = "https://api.open-meteo.com/v1/forecast"
WMO_WEATHER_CODES = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "depositing rime fog",
    51: "drizzle: light intensity",
    53: "drizzle: moderate intensity",
    55: "drizzle: dense intensity",
    56: "freezing drizzle: light intensity",
    57: "freezing drizzle: dense intensity",
    61: "rain: slight intensity",
    63: "rain: moderate intensity",
    65: "rain: heavy intensity",
    66: "freezing rain: light intensity",
    67: "freezing rain: heavy intensity",
    71: "snow fall: slight intensity",
    73: "snow fall: moderate intensity",
    75: "snow fall: heavy intensity",
    77: "snow grains",
    80: "rain showers: slight",
    81: "rain showers: moderate",
    82: "rain showers: violent",
    85: "snow showers: slight",
    86: "snow showers: heavy",
    95: "thunderstorm",
    96: "thunderstorm with slight hail",
    99: "thunderstorm with heavy hail"
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
    filtered_weather_data = {
        "weather_code": WMO_WEATHER_CODES[data["current"]["weather_code"]],
        "temperature_2m": data["current"]["temperature_2m"],
        "apparent_temperature": data["current"]["apparent_temperature"],
        "wind_speed_10m": data["current"]["wind_speed_10m"],
        "precipitation_probability": data["current"]["precipitation_probability"],
        "precipitation": data["current"]["precipitation"],
        "uv_index_max": data["daily"]["uv_index_max"][0],
        "sunrise": data["daily"]["sunrise"][0],
        "sunset": data["daily"]["sunset"][0],
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

    return filtered_data # response.json()

