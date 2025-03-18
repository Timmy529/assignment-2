""" test_bmi_calculator.py
This module contains unit tests for the determine_category function in bmi_calculator.py.
"""
import pytest
from bmi_calculator import determine_category
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
