from pydantic import BaseModel

class Interaction(BaseModel):
    hcp_name: str
    hospital: str
    specialization: str
    notes: str