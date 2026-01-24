# backend/main.py

from fastapi import FastAPI
from backend.api.chat import router as chat_router
from backend.api.health import router as health_router
from backend.api.projects import router as projects_router




app = FastAPI(title="AI Project Lab")

app.include_router(chat_router, prefix="/api")
app.include_router(health_router, prefix="/api")
app.include_router(projects_router, prefix="/api")