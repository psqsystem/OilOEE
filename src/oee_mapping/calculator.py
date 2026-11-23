"""OEE calculation utilities."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OEEInputs:
    planned_production_minutes: float
    downtime_minutes: float
    ideal_cycle_time_seconds: float
    total_units: int
    good_units: int

    def __post_init__(self) -> None:
        if self.planned_production_minutes <= 0:
            raise ValueError("planned_production_minutes must be > 0")
        if self.downtime_minutes < 0:
            raise ValueError("downtime_minutes must be >= 0")
        if self.downtime_minutes > self.planned_production_minutes:
            raise ValueError("downtime cannot exceed planned production time")
        if self.ideal_cycle_time_seconds <= 0:
            raise ValueError("ideal_cycle_time_seconds must be > 0")
        if self.total_units < 0 or self.good_units < 0:
            raise ValueError("unit counts must be >= 0")
        if self.good_units > self.total_units:
            raise ValueError("good_units cannot exceed total_units")


def availability(planned_minutes: float, downtime_minutes: float) -> float:
    """Availability = (Planned - Downtime) / Planned."""
    return (planned_minutes - downtime_minutes) / planned_minutes


def performance(
    run_minutes: float,
    ideal_cycle_time_seconds: float,
    total_units: int,
) -> float:
    """Performance = (Ideal Cycle Time * Total Units) / Run Time.

    Returns 0.0 when run_minutes is zero.
    """
    if run_minutes <= 0:
        return 0.0
    return (ideal_cycle_time_seconds * total_units) / (run_minutes * 60.0)


def quality(total_units: int, good_units: int) -> float:
    """Quality = Good Units / Total Units. Returns 0.0 when total is zero."""
    if total_units == 0:
        return 0.0
    return good_units / total_units


def compute_oee(inputs: OEEInputs) -> dict[str, float]:
    """Compute OEE and its components from raw inputs."""
    run_minutes = inputs.planned_production_minutes - inputs.downtime_minutes
    a = availability(inputs.planned_production_minutes, inputs.downtime_minutes)
    p = performance(run_minutes, inputs.ideal_cycle_time_seconds, inputs.total_units)
    q = quality(inputs.total_units, inputs.good_units)
    return {
        "availability": a,
        "performance": p,
        "quality": q,
        "oee": a * p * q,
    }
