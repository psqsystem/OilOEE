"""Tests for OEE calculation and work-order model."""

from datetime import datetime, timezone

import pytest

from src.ingestion.models import WorkOrder
from src.oee_mapping.calculator import OEEInputs, availability, compute_oee, performance, quality


def test_availability_basic():
    assert availability(480, 48) == pytest.approx(0.9)


def test_availability_invalid_inputs():
    with pytest.raises(ValueError):
        OEEInputs(
            planned_production_minutes=0,
            downtime_minutes=0,
            ideal_cycle_time_seconds=30,
            total_units=0,
            good_units=0,
        )


def test_performance_zero_run_time():
    assert performance(0, 30, 100) == 0.0


def test_quality_zero_total():
    assert quality(0, 0) == 0.0


def test_compute_oee_full():
    inputs = OEEInputs(
        planned_production_minutes=480,
        downtime_minutes=48,
        ideal_cycle_time_seconds=1,
        total_units=432,
        good_units=410,
    )
    result = compute_oee(inputs)
    assert result["availability"] == pytest.approx(0.9, rel=1e-6)
    assert result["performance"] == pytest.approx(0.9, rel=1e-6)
    assert result["quality"] == pytest.approx(410 / 432, rel=1e-6)
    assert 0 < result["oee"] < 1


def test_work_order_minimal_valid():
    wo = WorkOrder(
        work_order_id="WO-0001",
        equipment_id="EQ-101",
        site_id="SITE-A",
        shift="day",
        event_timestamp=datetime(2026, 1, 15, 8, 0, tzinfo=timezone.utc),
        description="Pump seal leak detected during routine inspection.",
        downtime_minutes=45,
        oee_component=["availability"],
        failure_mode="seal_leak",
        severity="moderate",
        supervisor_validated=True,
    )
    assert wo.downtime_minutes == 45
    assert wo.shift.value == "day"


def test_work_order_rejects_real_name_in_validated_by():
    with pytest.raises(ValueError):
        WorkOrder(
            work_order_id="WO-0002",
            equipment_id="EQ-101",
            site_id="SITE-A",
            shift="night",
            event_timestamp=datetime(2026, 1, 15, 22, 0, tzinfo=timezone.utc),
            description="Valve stuck.",
            downtime_minutes=10,
            oee_component=["performance"],
            failure_mode="valve_stuck",
            severity="minor",
            supervisor_validated=True,
            validated_by="John Smith",
        )
