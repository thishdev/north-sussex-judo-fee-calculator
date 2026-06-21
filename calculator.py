"""Monthly cost calculations for the North Sussex Judo application."""

from __future__ import annotations

from models import Athlete
from validation import (
    COMPETITION_ENTRY_FEE,
    PRIVATE_TUITION_PER_HOUR,
    TRAINING_PLANS,
    WEEKS_PER_MONTH,
    format_currency,
    get_weight_comparison,
)


class CostCalculator:
    """Calculate monthly fees and weight comparisons for an athlete."""

    def calculate_training_cost(self, training_plan: str) -> float:
        """Calculate the monthly training cost for a plan."""

        return TRAINING_PLANS[training_plan] * WEEKS_PER_MONTH

    def calculate_competition_cost(self, competitions: int) -> float:
        """Calculate the competition entry cost for the month."""

        return competitions * COMPETITION_ENTRY_FEE

    def calculate_private_coaching_cost(self, private_coaching_hours: float) -> float:
        """Calculate the monthly private coaching cost."""

        return private_coaching_hours * PRIVATE_TUITION_PER_HOUR * WEEKS_PER_MONTH

    def calculate_total_monthly_cost(self, athlete: Athlete) -> float:
        """Calculate the total monthly cost for an athlete."""

        training_cost = self.calculate_training_cost(athlete.training_plan)
        competition_cost = self.calculate_competition_cost(athlete.competitions)
        coaching_cost = self.calculate_private_coaching_cost(athlete.private_coaching_hours)
        return training_cost + competition_cost + coaching_cost

    def get_weight_comparison(self, current_weight: float, weight_category: str) -> str:
        """Return the weight comparison message for the chosen category."""

        return get_weight_comparison(current_weight, weight_category)

    def build_breakdown(self, athlete: Athlete) -> dict[str, str]:
        """Return a formatted cost breakdown for the GUI."""

        training_cost = self.calculate_training_cost(athlete.training_plan)
        competition_cost = self.calculate_competition_cost(athlete.competitions)
        coaching_cost = self.calculate_private_coaching_cost(athlete.private_coaching_hours)
        total_cost = training_cost + competition_cost + coaching_cost

        return {
            "athlete": athlete.name,
            "training_plan": athlete.training_plan,
            "training_cost": format_currency(training_cost),
            "competitions": str(athlete.competitions),
            "competition_cost": format_currency(competition_cost),
            "private_coaching_hours": str(athlete.private_coaching_hours),
            "private_coaching_cost": format_currency(coaching_cost),
            "total_cost": format_currency(total_cost),
            "weight_check": self.get_weight_comparison(
                athlete.current_weight, athlete.weight_category
            ),
        }
