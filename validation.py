"""Validation and small reusable helper functions."""

from __future__ import annotations

from typing import Final

TRAINING_PLANS: Final[dict[str, float]] = {
    "Beginner": 25.0,
    "Intermediate": 30.0,
    "Elite": 35.0,
}

WEIGHT_CATEGORIES: Final[dict[str, float | None]] = {
    "Flyweight": 66.0,
    "Lightweight": 73.0,
    "Light-Middleweight": 81.0,
    "Middleweight": 90.0,
    "Light-Heavyweight": 100.0,
    "Heavyweight": None,
}

WEEKS_PER_MONTH: Final[int] = 4
PRIVATE_TUITION_PER_HOUR: Final[float] = 9.50
COMPETITION_ENTRY_FEE: Final[float] = 22.0
MAX_PRIVATE_COACHING_HOURS: Final[float] = 5.0


def format_currency(amount: float) -> str:
    """Format a number as GBP currency."""

    return f"£{amount:.2f}"


def validate_name(name: str) -> str:
    """Return a cleaned athlete name or raise ValueError."""

    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Athlete name is required.")
    return cleaned


def validate_training_plan(training_plan: str) -> str:
    """Return a valid training plan or raise ValueError."""

    if training_plan not in TRAINING_PLANS:
        raise ValueError("Training plan must be selected.")
    return training_plan


def validate_weight(weight_text: str) -> float:
    """Return a positive weight value or raise ValueError."""

    try:
        weight = float(weight_text)
    except ValueError as exc:
        raise ValueError("Current weight must be a positive number.") from exc

    if weight <= 0:
        raise ValueError("Current weight must be a positive number.")
    return weight


def validate_weight_category(weight_category: str) -> str:
    """Return a valid competition weight category or raise ValueError."""

    if weight_category not in WEIGHT_CATEGORIES:
        raise ValueError("Weight category must be selected.")
    return weight_category


def validate_competitions(competitions_text: str) -> int:
    """Return a whole number of competitions or raise ValueError."""

    try:
        competitions = int(competitions_text)
    except ValueError as exc:
        raise ValueError(
            "Competitions must be a whole number greater than or equal to 0."
        ) from exc

    if competitions < 0:
        raise ValueError("Competitions must be a whole number greater than or equal to 0.")
    return competitions


def validate_private_coaching_hours(hours_text: str) -> float:
    """Return private coaching hours between 0 and 5 inclusive."""

    try:
        hours = float(hours_text)
    except ValueError as exc:
        raise ValueError("Private coaching hours must be a number between 0 and 5.") from exc

    if hours < 0 or hours > MAX_PRIVATE_COACHING_HOURS:
        raise ValueError("Private coaching hours must be a number between 0 and 5.")
    return hours


def validate_competition_eligibility(training_plan: str, competitions: int) -> None:
    """Prevent beginner athletes from entering competitions."""

    if training_plan == "Beginner" and competitions > 0:
        raise ValueError("Beginner athletes cannot enter competitions.")


def get_weight_comparison(current_weight: float, weight_category: str) -> str:
    """Describe how the current weight compares with the selected category."""

    limit = WEIGHT_CATEGORIES[weight_category]

    if weight_category == "Heavyweight":
        if current_weight > 100.0:
            return "Current weight is within the Heavyweight category."
        return "Current weight is below the Heavyweight category threshold."

    assert limit is not None

    if current_weight <= limit:
        return f"Current weight is within the {weight_category} category."

    difference = current_weight - limit
    return f"Current weight is {difference:.2f} kg above the {weight_category} limit."
