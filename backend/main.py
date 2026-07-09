from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from database.db import engine, Base
from models.interaction_table import InteractionTable
from routes.interaction_routes import router
app = FastAPI(
    title="AI-First CRM HCP Module",
    description="Backend API for HCP Interaction Logging",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
   allow_origins=[
    "http://localhost:5173",
    "http://localhost:5174",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
@app.get("/")
def home():
    return {
        "message": "Welcome to AI-First CRM - HCP Backend"
    }

@app.get("/health")
def health():
    return {
        "status": "Backend is running successfully"
    }