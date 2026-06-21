"""Tkinter GUI for the North Sussex Judo fee calculator."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable

from calculator import CostCalculator
from models import Athlete
from validation import (
    TRAINING_PLANS,
    WEIGHT_CATEGORIES,
    validate_competition_eligibility,
    validate_competitions,
    validate_name,
    validate_private_coaching_hours,
    validate_training_plan,
    validate_weight,
    validate_weight_category,
)


class NorthSussexJudoApp:
    """Main application window."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.calculator = CostCalculator()
        self.root.title("North Sussex Judo Fee Calculator")
        self.root.geometry("760x620")
        self.root.minsize(720, 600)

        self.name_var = tk.StringVar()
        self.training_plan_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.weight_category_var = tk.StringVar()
        self.competitions_var = tk.StringVar()
        self.coaching_hours_var = tk.StringVar()

        self._build_widgets()

    def _build_widgets(self) -> None:
        container = ttk.Frame(self.root, padding=18)
        container.pack(fill="both", expand=True)

        title = ttk.Label(
            container,
            text="North Sussex Judo Fee Calculator",
            font=("TkDefaultFont", 16, "bold"),
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 14))

        subtitle = ttk.Label(
            container,
            text="Enter the athlete details and calculate monthly fees.",
        )
        subtitle.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 18))

        self._add_label_entry(container, "Athlete name", self.name_var, 2)
        self._add_label_combobox(
            container,
            "Training plan",
            self.training_plan_var,
            tuple(TRAINING_PLANS.keys()),
            3,
            self._on_training_plan_change,
        )
        self._add_label_entry(container, "Current weight (kg)", self.weight_var, 4)
        self._add_label_combobox(
            container,
            "Competition weight category",
            self.weight_category_var,
            tuple(WEIGHT_CATEGORIES.keys()),
            5,
        )
        self._add_label_entry(container, "Competitions this month", self.competitions_var, 6)
        self._add_label_entry(
            container,
            "Private coaching hours per week",
            self.coaching_hours_var,
            7,
        )

        button_frame = ttk.Frame(container)
        button_frame.grid(row=8, column=0, columnspan=2, sticky="w", pady=(8, 16))

        calculate_button = ttk.Button(button_frame, text="Calculate", command=self.calculate)
        calculate_button.pack(side="left", padx=(0, 10))

        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_form)
        clear_button.pack(side="left")

        results_label = ttk.Label(container, text="Results")
        results_label.grid(row=9, column=0, columnspan=2, sticky="w")

        self.result_text = tk.Text(container, height=18, wrap="word")
        self.result_text.grid(row=10, column=0, columnspan=2, sticky="nsew", pady=(6, 0))
        self.result_text.configure(state="disabled")

        scrollbar = ttk.Scrollbar(container, command=self.result_text.yview)
        scrollbar.grid(row=10, column=2, sticky="ns", pady=(6, 0))
        self.result_text.configure(yscrollcommand=scrollbar.set)

        container.columnconfigure(1, weight=1)
        container.rowconfigure(10, weight=1)

    def _add_label_entry(
        self, parent: ttk.Frame, label_text: str, variable: tk.StringVar, row: int
    ) -> None:
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky="w", pady=6)

        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=1, sticky="ew", pady=6)

    def _add_label_combobox(
        self,
        parent: ttk.Frame,
        label_text: str,
        variable: tk.StringVar,
        values: tuple[str, ...],
        row: int,
        callback: Callable[[tk.Event], None] | None = None,
    ) -> None:
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky="w", pady=6)

        combobox = ttk.Combobox(parent, textvariable=variable, values=values, state="readonly")
        combobox.grid(row=row, column=1, sticky="ew", pady=6)
        combobox.set("")

        if callback is not None:
            combobox.bind("<<ComboboxSelected>>", callback)

    def _on_training_plan_change(self, event: tk.Event | None = None) -> None:
        """Clear stale results when the training plan changes."""

        self._clear_result_area()

    def calculate(self) -> None:
        """Validate the form and display a full cost breakdown."""

        try:
            name = validate_name(self.name_var.get())
            training_plan = validate_training_plan(self.training_plan_var.get())
            current_weight = validate_weight(self.weight_var.get())
            weight_category = validate_weight_category(self.weight_category_var.get())
            competitions = validate_competitions(self.competitions_var.get())
            coaching_hours = validate_private_coaching_hours(self.coaching_hours_var.get())
            validate_competition_eligibility(training_plan, competitions)

            athlete = Athlete(
                name=name,
                training_plan=training_plan,
                current_weight=current_weight,
                weight_category=weight_category,
                competitions=competitions,
                private_coaching_hours=coaching_hours,
            )
            breakdown = self.calculator.build_breakdown(athlete)
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))
            return

        self._display_results(breakdown)

    def clear_form(self) -> None:
        """Clear all form fields and the results panel."""

        self.name_var.set("")
        self.training_plan_var.set("")
        self.weight_var.set("")
        self.weight_category_var.set("")
        self.competitions_var.set("")
        self.coaching_hours_var.set("")
        self._clear_result_area()

    def _display_results(self, breakdown: dict[str, str]) -> None:
        lines = [
            f"Athlete: {breakdown['athlete']}",
            "",
            "Monthly Cost Breakdown:",
            f"Training Plan: {breakdown['training_plan']}",
            f"Training Cost: {breakdown['training_cost']}",
            f"Competition Entries: {breakdown['competitions']}",
            f"Competition Cost: {breakdown['competition_cost']}",
            f"Private Coaching: {breakdown['private_coaching_hours']} hours per week",
            f"Private Coaching Cost: {breakdown['private_coaching_cost']}",
            "",
            f"Total Monthly Cost: {breakdown['total_cost']}",
            "",
            "Weight Check:",
            breakdown["weight_check"],
        ]
        self._set_result_text("\n".join(lines))

    def _clear_result_area(self) -> None:
        self._set_result_text("")

    def _set_result_text(self, text: str) -> None:
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", text)
        self.result_text.configure(state="disabled")


def run_app() -> None:
    """Start the Tkinter application."""

    root = tk.Tk()
    app = NorthSussexJudoApp(root)
    root.mainloop()
