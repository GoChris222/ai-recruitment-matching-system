from pydantic import BaseModel
from typing import List, Optional


class Vacancy(BaseModel):
    id: str

    client: str

    location: str
    state: str

    role_type: str

    start_date: str
    end_date: str

    block_length_days: int

    rate: Optional[int] = None
    rate_type: str = "daily"

    travel_included: bool = False
    accommodation_included: bool = False
    car_included: bool = False

    skills_required: List[str] = []

    rural_remote: bool = False
    fifo_available: bool = False

    urgency: str = "medium"

    raw_text: Optional[str] = None

    notes: Optional[str] = None
