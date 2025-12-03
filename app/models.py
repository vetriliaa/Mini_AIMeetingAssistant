from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    meetings = relationship("Meeting", back_populates="owner")

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    transcript = Column(Text)
    duration_minutes = Column(Integer)
    participant_count = Column(Integer)

    # AI insights, stored as JSON file
    action_items = Column(JSON)
    key_decisions = Column(JSON)
    sentiment_score = Column(Integer)
    topics = Column(JSON)

    created_at = Column(DateTime, default=datetime.now)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="meetings")