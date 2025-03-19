""" test_bmi_calculator.py
This module contains unit tests for the calculate_bmi and determine_category function in bmi_calculator.py.
"""
import pytest
from bmi_calculator import determine_category, calculate_bmi

@pytest.mark.parametrize("height, weight, expected_bmi", [
    (65, 100, 17.0),  # Underweight
    (70, 150, 22.0),  # Normal weight
    (68, 180, 28.0),  # Overweight
    (65, 200, 34),  # Obese
])
def test_calculate_bmi(height, weight, expected_bmi):
    assert calculate_bmi(height, weight) == pytest.approx(expected_bmi, rel=1e-2)


@pytest.mark.parametrize("bmi, expected_category", [

    # Test cases for Underweight category
    (18.3, "Underweight"),  # Internal point
    (18.4, "Underweight"),  # Upper bound
    (18.5, "Normal weight"),  # Just above upper bound

    # Test cases for Normal weight category
    (18.4, "Underweight"),  # Just under lower bound
    (18.5, "Normal weight"),  # Lower bound
    (22.0, "Normal weight"),  # Internal point
    (24.9, "Normal weight"),  # Upper bound
    (25.0, "Overweight"),  # Just above upper bound

    # Test cases for Overweight category
    (24.9, "Normal weight"),  # Just under lower bound
    (25.0, "Overweight"),  # Lower bound
    (27.5, "Overweight"),  # Internal point
    (29.9, "Overweight"),  # Upper bound
    (30.0, "Obese"),  # Just above upper bound

    # Test cases for Obese category
    (29.9, "Overweight"),  # Just under lower bound
    (30.0, "Obese"),  # Lower bound
    (30.1, "Obese"),  # Internal point

])
def test_determine_category(bmi, expected_category):
    assert determine_category(bmi) == expected_category
