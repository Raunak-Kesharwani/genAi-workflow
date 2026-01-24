# backend/tools/weather_tools.py

import requests
from langchain.tools import tool


@tool
def get_weather_for_location(city: str) -> str:
    """
    Get real weather for a city using Open-Meteo API.
    """
    try:
        geo_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1"
        )
        geo_resp = requests.get(geo_url, timeout=5).json()

        if not geo_resp.get("results"):
            return f"Could not find weather data for {city}"

        lat = geo_resp["results"][0]["latitude"]
        lon = geo_resp["results"][0]["longitude"]

        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )
        weather_resp = requests.get(weather_url, timeout=5).json()
        current = weather_resp.get("current_weather")

        if not current:
            return f"Weather data unavailable for {city}"

        temp = current["temperature"]
        wind = current["windspeed"]

        return (
            f"Current temperature in {city} is {temp}°C "
            f"with wind speed {wind} km/h."
        )

    except Exception:
        return f"Failed to fetch weather for {city}"
