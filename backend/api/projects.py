# backend/api/projects.py

from fastapi import APIRouter
from backend.projects.registry import list_projects

router = APIRouter()


@router.get("/projects")
def get_projects():
    return list_projects()
