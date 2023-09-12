from tabulate import tabulate

from styles import stylize


def calories_intake_per_day(weight: float, height: float, age: float, human_activity_indicator: float,
                            male_or_female: str):
    """
        Calculate the daily calorie intake based on user's weight, height, age, activity level, and gender.

        Args:
        - weight (float): User's weight in kilograms.
        - height (float): User's height in centimeters.
        - age (float): User's age in years.
        - human_activity_indicator (float): Activity level indicator based on a scale.
        - male_or_female (str): User's gender, either 'male' or 'female'.

        Returns:
        - calories (float): The estimated daily calorie intake based on the provided inputs.
        """
    if male_or_female == "male":
        calories = ((((weight * 10) + (6.25 * height)) - (5 * age + 5)) * human_activity_indicator)
    elif male_or_female == "female":
        calories = ((((weight * 10) + (6.25 * height)) - (5 * age - 161)) * human_activity_indicator)
    return calories


def protein_fats_carbohydrates(weight: float, calories: float):
    """
        Calculate the recommended daily intake of proteins, fats, and carbohydrates based on weight and calorie intake.

        Args:
        - weight (float): User's weight in kilograms.
        - calories (float): User's estimated daily calorie intake.

        Returns:
        - proteins (float): Recommended daily intake of proteins in grams.
        - fats (float): Recommended daily intake of fats in grams.
        - carbohydrates (float): Recommended daily intake of carbohydrates in grams.
        """
    proteins = weight * 1.5
    fats = weight * 1
    # carbohydrates = (calories - ((proteins * 4) + fats * 9)) / 4
    if proteins < 160:
        proteins += 25
        fats += 12
    carbohydrates = (calories - ((proteins * 4) + fats * 9)) / 4
    return proteins, fats, carbohydrates


def main():
    print(stylize("\nWelcome to the protein, fats, and carbohydrates calculator!", 'white', 'bold'))
    print("Okay, now let’s calculate your daily calorie intake ᕦ( ͡° ͜ʖ ͡°)ᕤ")

    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            break  # Exit the loop on successful weight input
        except ValueError:
            print(stylize("Incorrect weight value entered. Please re-enter your weight.", 'red'))

    # Ask for height, age, activity level, and gender
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            break  # Exit the loop on successful height input
        except ValueError:
            print(stylize("Incorrect height value entered. Please re-enter your height.", 'red'))

    while True:
        try:
            age = float(input("Enter your age: "))
            break  # Exit the loop on successful age input
        except ValueError:
            print(stylize("Incorrect age value entered. Please re-enter your age.", 'red'))

    male_or_female = None
    while male_or_female not in ["male", "female"]:
        if male_or_female is not None:
            print(stylize("Invalid input. Please enter 'male' or 'female'.", 'red'))
        male_or_female = input("Are you a male or a female? (male/female): ").lower().strip()

    activity_indicator = (
        ("almost no activity, sedentary lifestyle, no sports", 1.2),
        ("low activity. Sedentary lifestyle and some sports - up to three low-intensity workouts per week", 1.375),
        ("moderate activity. To select this ratio, a person should train three to four times a week, with "
            "intense but not hard workouts", 1.55),
        ("high activity. These are daily sports activities or daily work associated with a lot of movement "
            "and manual labor, e.g., farming", 1.7),
        ("extreme activity. This is more likely for professional athletes and people with active jobs like "
            "working with weights, etc.", 1.9),
    )

    while True:
        print(stylize("Activity indicators:", '', 'bold'))
        [print(f"{i} - {app[0]}") for i, app in enumerate(activity_indicator, 1)]
        user_input = input("Enter a number: ")

        try:
            human_activity_indicator = activity_indicator[int(user_input) - 1][1]
            break
        except IndexError:
            print(stylize(f"Please enter a number from 1 to {len(activity_indicator)}\n", 'red'))
        except ValueError:
            print(stylize(f"Please enter a number\n", 'red'))

    # Calculate the user's daily calorie intake
    calories = calories_intake_per_day(weight, height, age, human_activity_indicator, male_or_female)

    print(stylize(f"Your daily calorie intake is: {calories:.2f} calories", 'green'))

    proteins, fats, carbohydrates = protein_fats_carbohydrates(weight, calories)

    headers = ["Proteins per day", "Fats per day", "Carbohydrates per day", "Calories intake per day"]
    data = [[proteins, fats, carbohydrates, calories]]
    colalign = ("center", "center", "center", "center")
    table = tabulate(data, headers, tablefmt="grid", colalign=colalign)
    print(table)
    print(stylize("NOW LETS GO TO THE GYM!!!\n", 'cyan'))
