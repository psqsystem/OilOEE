"""Pydantic models for work-order ingestion."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class Shift(str, Enum):
    day = "day"
    swing = "swing"
    night = "night"


class OEEComponent(str, Enum):
    availability = "availability"
    performance = "performance"
    quality = "quality"
    non_oee = "non-oee"


class Severity(str, Enum):
    minor = "minor"
    moderate = "moderate"
    major = "major"


class Confidence(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class WorkOrder(BaseModel):
    """A single industrial work-order report aligned with OEE components."""

    work_order_id: str = Field(min_length=1)
    equipment_id: str = Field(min_length=1)
    site_id: str = Field(min_length=1)
    shift: Shift
    event_timestamp: datetime
    description: str = Field(min_length=1, max_length=2000)
    action_taken: Optional[str] = Field(default=None, max_length=2000)
    downtime_minutes: int = Field(ge=0)
    oee_component: List[OEEComponent] = Field(min_length=1)
    failure_mode: str = Field(min_length=1)
    severity: Severity
    confidence: Optional[Confidence] = None
    supervisor_validated: bool
    validated_by: Optional[str] = None
    validated_at: Optional[datetime] = None
    notes: Optional[str] = Field(default=None, max_length=1000)

    @field_validator("validated_by")
    @classmethod
    def no_real_names(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and " " in v.strip():
            raise ValueError("validated_by must be an anonymized identifier, not a real name")
        return v

    model_config = {"extra": "forbid"}
