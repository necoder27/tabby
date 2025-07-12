from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.os_info import get_disk_usage_info, get_macos_version_info, get_memory_usage_info, get_uptime_info
from backend.personal_info import get_greeting_based_on_daytime, get_location_from_ip_address
from backend.weather_data import WeatherResponse, get_weather_data
from typing import Any


api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://tabby.dashboard:5173", "http://tabby.dashboard:7777", "http://localhost:8888", "http://tabby.dashboard:8888"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
def get_macos_version() -> str:
    return get_macos_version_info()

@api.get("/system/uptime")
def get_uptime() -> str:
    return get_uptime_info()

@api.get("/system/memory")
def get_memory_usage() -> str:
    return get_memory_usage_info()

@api.get("/system/disk")
def get_disk_usage() -> str:
    return get_disk_usage_info()
