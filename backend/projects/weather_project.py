# backend/projects/weather_project.py

from backend.projects.base import BaseProject
from backend.agents.response_schemas import WeatherResponse
from backend.agents.prompts import WEATHER_SYSTEM_PROMPT
from backend.tools.weather_tools import get_weather_for_location
from backend.tools.user_tools import get_user_location


class WeatherProject(BaseProject):

    @property
    def project_id(self) -> str:
        return "weather"

    @property
    def name(self) -> str:
        return "Weather Agent"

    @property
    def description(self) -> str:
        return "Detects your location and fetches real-time weather."

    @property
    def system_prompt(self) -> str:
        return WEATHER_SYSTEM_PROMPT

    @property
    def tools(self):
        return [
            get_user_location,
            get_weather_for_location
        ]

    @property
    def response_schema(self):
        return WeatherResponse

