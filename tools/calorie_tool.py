from langchain.tools import tool

@tool
def calculate_calories(weight: float, height: float, age: int, gender: str, activity_level: str) -> str:
    """Estimates daily calorie needs based on weight, height, age, gender, and activity level."""
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    multiplier = {
        "low": 1.2,
        "medium": 1.55,
        "high": 1.9
    }.get(activity_level.lower(), 1.2)

    return f"Your estimated daily calorie needs are {int(bmr * multiplier)} kcal."
