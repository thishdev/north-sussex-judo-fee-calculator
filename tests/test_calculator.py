"""Unit tests for the North Sussex Judo calculator."""

from __future__ import annotations

import unittest

from calculator import CostCalculator
from models import Athlete
from validation import (
    validate_competition_eligibility,
    validate_private_coaching_hours,
)


class TestCostCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = CostCalculator()

    def test_beginner_monthly_training_cost(self) -> None:
        self.assertEqual(self.calculator.calculate_training_cost("Beginner"), 100.0)

    def test_intermediate_monthly_training_cost(self) -> None:
        self.assertEqual(self.calculator.calculate_training_cost("Intermediate"), 120.0)

    def test_elite_monthly_training_cost(self) -> None:
        self.assertEqual(self.calculator.calculate_training_cost("Elite"), 140.0)

    def test_competition_cost(self) -> None:
        self.assertEqual(self.calculator.calculate_competition_cost(2), 44.0)

    def test_private_coaching_cost(self) -> None:
        self.assertEqual(self.calculator.calculate_private_coaching_cost(3.0), 114.0)

    def test_total_monthly_cost(self) -> None:
        athlete = Athlete("Sarah Jones", "Intermediate", 70.0, "Lightweight", 2, 3.0)
        self.assertEqual(self.calculator.calculate_total_monthly_cost(athlete), 278.0)

    def test_beginner_cannot_enter_competitions(self) -> None:
        with self.assertRaises(ValueError):
            validate_competition_eligibility("Beginner", 1)

    def test_private_coaching_cannot_exceed_five_hours(self) -> None:
        with self.assertRaises(ValueError):
            validate_private_coaching_hours("5.1")

    def test_weight_comparison_within_category(self) -> None:
        message = self.calculator.get_weight_comparison(70.0, "Lightweight")
        self.assertEqual(message, "Current weight is within the Lightweight category.")

    def test_weight_comparison_above_category(self) -> None:
        message = self.calculator.get_weight_comparison(94.5, "Middleweight")
        self.assertEqual(message, "Current weight is 4.50 kg above the Middleweight limit.")

    def test_weight_comparison_heavyweight(self) -> None:
        within_message = self.calculator.get_weight_comparison(101.0, "Heavyweight")
        below_message = self.calculator.get_weight_comparison(100.0, "Heavyweight")
        self.assertEqual(within_message, "Current weight is within the Heavyweight category.")
        self.assertEqual(
            below_message, "Current weight is below the Heavyweight category threshold."
        )

    def test_weight_comparison_lightweight_120kg(self) -> None:
        message = self.calculator.get_weight_comparison(120.0, "Lightweight")
        self.assertEqual(message, "Current weight is 47.00 kg above the Lightweight limit.")

    def test_weight_comparison_lightweight_72kg(self) -> None:
        message = self.calculator.get_weight_comparison(72.0, "Lightweight")
        self.assertEqual(message, "Current weight is within the Lightweight category.")

    def test_weight_comparison_middleweight_95kg(self) -> None:
        message = self.calculator.get_weight_comparison(95.0, "Middleweight")
        self.assertEqual(message, "Current weight is 5.00 kg above the Middleweight limit.")

    def test_weight_comparison_heavyweight_120kg(self) -> None:
        message = self.calculator.get_weight_comparison(120.0, "Heavyweight")
        self.assertEqual(message, "Current weight is within the Heavyweight category.")

    def test_weight_comparison_heavyweight_90kg(self) -> None:
        message = self.calculator.get_weight_comparison(90.0, "Heavyweight")
        self.assertEqual(
            message, "Current weight is below the Heavyweight category threshold."
        )

    def test_breakdown_includes_weight_check(self) -> None:
        athlete = Athlete("Test", "Intermediate", 120.0, "Lightweight", 2, 2.0)
        breakdown = self.calculator.build_breakdown(athlete)
        self.assertEqual(
            breakdown["weight_check"],
            "Current weight is 47.00 kg above the Lightweight limit.",
        )


if __name__ == "__main__":
    unittest.main()
