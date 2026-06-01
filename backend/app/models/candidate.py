from pydantic import BaseModel
from typing import List


class AvailabilityWindow(BaseModel):
    start_date: str
    end_date: str


class EngagementMetrics(BaseModel):
    average_reply_hours: float
    last_contact_date: str
    reliability_score: int
    ghost_count: int
    ghost_rate: float


class PlacementHistory(BaseModel):
    placements_completed: int
    placements_accepted: int
    placements_declined: int
    acceptance_rate: float


class Candidate(BaseModel):
    id: str
    name: str
    registration_status: str

    role_types: List[str]
    skills: List[str]

    preferred_states: List[str]
    avoided_states: List[str]

    preferred_locations: List[str]
    avoided_locations: List[str]

    preferred_rate_min: float
    preferred_rate_target: float

    availability: List[AvailabilityWindow]

    fifo_preference: bool
    rural_remote_preference: str

    engagement: EngagementMetrics
    history: PlacementHistory

    inferred_preferences: List[str]

    notes: str
