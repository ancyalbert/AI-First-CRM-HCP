from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ai_agent.agent import ask_ai
from database.db import SessionLocal
from models.interaction_model import Interaction
from models.interaction_table import InteractionTable

router = APIRouter()


# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Save Interaction
@router.post("/log-interaction")
def log_interaction(data: Interaction, db: Session = Depends(get_db)):

    interaction = InteractionTable(
        hcp_name=data.hcp_name,
        hospital=data.hospital,
        specialization=data.specialization,
        notes=data.notes,
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "message": "Interaction logged successfully",
        "data": interaction,
    }


# Get All Interactions
@router.get("/interactions")
def get_interactions(db: Session = Depends(get_db)):

    interactions = db.query(InteractionTable).all()

    return interactions


# Chat Request Model
class ChatRequest(BaseModel):
    message: str


# AI Chat API
@router.post("/chat")
def chat(request: ChatRequest):

    reply = ask_ai(request.message)

    return {
        "reply": reply
    }