# backend/projects/registry.py

from typing import Dict
from backend.projects.base import BaseProject
from backend.projects.weather_project import WeatherProject

_PROJECT_REGISTRY: Dict[str, BaseProject] = {
    "weather": WeatherProject(),
}


def get_project(project_id: str) -> BaseProject:
    if project_id not in _PROJECT_REGISTRY:
        raise ValueError(f"Unknown project_id: {project_id}")
    return _PROJECT_REGISTRY[project_id]


def list_projects():
    """
    Used by frontend to show landing page projects.
    """
    return [
        {
            "project_id": project.project_id,
            "name": project.name,
            "description": project.description,
        }
        for project in _PROJECT_REGISTRY.values()
    ]
