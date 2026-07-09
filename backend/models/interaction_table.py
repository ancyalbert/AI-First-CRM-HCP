from sqlalchemy import Column, Integer, String

from database.db import Base


class InteractionTable(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255))
    hospital = Column(String(255))
    specialization = Column(String(255))
    notes = Column(String(1000))