# app/routers/meetings.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from ..services.ai_service import MeetingAnalyzer
from ..auth import get_current_user
import os

router = APIRouter(prefix="/meetings", tags=["meetings"])
analyzer = MeetingAnalyzer(api_key=os.getenv("ANTHROPIC_API_KEY"))

@router.post("/", response_model=schemas.MeetingResponse)
async def create_meeting(
    meeting: schemas.MeetingCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Upload a meeting transcript and get AI insights
    """
    # Analyze transcript with Claude
    insights = analyzer.analyze_transcript(meeting.transcript)
    
    # Create database record
    db_meeting = models.Meeting(
        title=meeting.title,
        transcript=meeting.transcript,
        duration_minutes=meeting.duration_minutes,
        participant_count=meeting.participant_count,
        action_items=insights["action_items"],
        key_decisions=insights["key_decisions"],
        sentiment_score=insights["sentiment_score"],
        topics=insights["topics"],
        owner_id=current_user.id
    )
    
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    
    return db_meeting

@router.get("/{meeting_id}", response_model=schemas.MeetingResponse)
async def get_meeting(
    meeting_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Retrieve a specific meeting with insights
    """
    meeting = db.query(models.Meeting).filter(
        models.Meeting.id == meeting_id,
        models.Meeting.owner_id == current_user.id
    ).first()
    
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    
    return meeting

@router.get("/", response_model=List[schemas.MeetingResponse])
async def list_meetings(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    List all meetings for current user
    """
    meetings = db.query(models.Meeting).filter(
        models.Meeting.owner_id == current_user.id
    ).offset(skip).limit(limit).all()
    
    return meetings