from pydantic import BaseModel
from typing import List


class Vacancy(BaseModel):
    id: str

    client: str

    location: str
    state: str

    role_type: str

    start_date: str
    end_date: str

    block_length_days: int

    rate: float
    rate_type: str

    travel_included: bool
    accommodation_included: bool
    car_included: bool

    skills_required: List[str]

    rural_remote: bool
    fifo_available: bool

    urgency: str

    raw_text: str

    notes: str
