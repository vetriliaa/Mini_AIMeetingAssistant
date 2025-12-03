# app/main.py
from fastapi import FastAPI
from .routers import meetings, auth
from .database import engine
from . import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Meeting Insights API")

# Include routers
app.include_router(auth.router)
app.include_router(meetings.router)

@app.get("/")
def read_root():
    return {"message": "Meeting Insights API - Powered by Claude AI"}