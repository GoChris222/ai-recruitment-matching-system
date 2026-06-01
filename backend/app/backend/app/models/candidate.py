from pydantic import BaseModel
from typing import List, Optional


class AvailabilityWindow(BaseModel):
    start_date: str
    end_date: str


class Engagement(BaseModel):
    average_reply_hours: Optional[float] = None
    last_contact_date: Optional[str] = None
    reliability_score: int = 70
    ghost_count: int = 0
    ghost_rate: float = 0.0


class CandidateHistory(BaseModel):
    placements_completed: int = 0
    placements_accepted: int = 0
    placements_declined: int = 0
    acceptance_rate: float = 0.5


class Candidate(BaseModel):
    id: str
    name: str
    registration_status: str

    role_types: List[str] = []
    skills: List[str] = []

    preferred_states: List[str] = []
    avoided_states: List[str] = []

    preferred_locations: List[str] = []
    avoided_locations: List[str] = []

    preferred_rate_min: Optional[int] = None
    preferred_rate_target: Optional[int] = None

    availability: List[AvailabilityWindow] = []

    fifo_preference: bool = False
    rural_remote_preference: str = "medium"

    engagement: Engagement
    history: CandidateHistory

    inferred_preferences: List[str] = []

    notes: Optional[str] = None
