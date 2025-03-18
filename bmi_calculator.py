""" bmi_calculator.py
This module contains functions to calculate the BMI and determine the BMI category.
"""

import argparse

def calculate_bmi(height_in, weight_lb):
    """
    Calculates the BMI based on the given height (in inches) and weight (in pounds),
    and determines the BMI category.
    :param height_in: Height in inches
    :param weight_lb: Weight in pounds
    :return: the BMI rounded to 1 decimal place
    """
    weight_kg = weight_lb * 0.45
    height_m = height_in * 0.025
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def determine_category(bmi):
    """
    Determines the BMI category based on the given BMI value.
    :param bmi: BMI value
    :return: the BMI category
    """
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    elif bmi >= 30:
        category = "Obese"
    else:
        category = "Invalid"
    return category


def main():
    parser = argparse.ArgumentParser(description="Calculate BMI and determine the category.")
    parser.add_argument("--height", type=float, required=True, help="Height in inches")
    parser.add_argument("--weight", type=float, required=True, help="Weight in pounds")

    args = parser.parse_args()

    bmi = calculate_bmi(args.height, args.weight)
    print(f"Your BMI: {bmi}")
    category = determine_category(bmi)
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
