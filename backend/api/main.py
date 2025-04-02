from fastapi import FastAPI
from backend.personal_info import get_greeting_based_on_daytime, get_location_from_ip_address
from backend.weather_data import WeatherResponse, get_weather_data

api = FastAPI()

@api.get("/greeting")
def get_greeting() -> str:
    return get_greeting_based_on_daytime()

@api.get("/location")
def get_location() -> str:
    return get_location_from_ip_address()

@api.get("/weather")
def get_weather() -> WeatherResponse:
    return get_weather_data()
