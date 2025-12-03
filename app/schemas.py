from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class MeetingCreate(BaseModel):
    title: str
    transcript: str
    duration_minutes: Optional[int] = None
    participant_count: Optional[int] = None

class MeetingResponse(BaseModel):
    id: int
    title: str
    transcript: str
    action_items: Optional[List[dict]] = None 
    key_decisions: Optional[List[str]] = None 
    sentiment_score: Optional[int] = None
    topics: Optional[List[str]] = None
    created_at: datetime

    class Config:
        from_attributes = True 

class UserCreate(BaseModel):
    email: str
    password: str 

class Token(BaseModel):
    access_token: str 
    token_type: str 

