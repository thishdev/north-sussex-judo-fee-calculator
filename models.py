"""Data models for the North Sussex Judo application."""

from dataclasses import dataclass


@dataclass(slots=True)
class Athlete:
    """Store the data entered for one athlete."""

    name: str
    training_plan: str
    current_weight: float
    weight_category: str
    competitions: int
    private_coaching_hours: float
