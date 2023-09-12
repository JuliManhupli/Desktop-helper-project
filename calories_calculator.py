from tabulate import tabulate



def calories_intake_per_day(weight: float, height: float, age: float, human_activity_indicator: float, male_or_female: str):
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


if __name__ == "__main__":

    print("Welcome to the protein, fats, and carbohydrates calculator")

    print("Okay, now let’s calculate your daily calorie intake ᕦ( ͡° ͜ʖ ͡°)ᕤ")

    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            break  # Exit the loop on successful weight input
        except ValueError:
            print("Error: Incorrect weight value entered. Please re-enter your weight.")

    # Ask for height, age, activity level, and gender
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            break  # Exit the loop on successful height input
        except ValueError:
            print("Error: Incorrect height value entered. Please re-enter your height.")

    while True:
        try:
            age = float(input("Enter your age: "))
            break  # Exit the loop on successful age input
        except ValueError:
            print("Error: Incorrect age value entered. Please re-enter your age.")

    male_or_female = None
    while male_or_female not in ["male", "female"]:
        if male_or_female is not None:
            print("Invalid input. Please enter 'male' or 'female'.")
        male_or_female = input("Are you a male or a female? (male/female): ").lower()

    while True:
        try:
            human_activity_indicator = float(input("""
Enter your activity indicator:
1.2 - almost no activity, sedentary lifestyle, no sports
1.375 - low activity. Sedentary lifestyle and some sports - up to three low-intensity workouts per week
1.55 - moderate activity. To select this ratio, a person should train three to four times a week, with intense but not hard workouts
1.7 - high activity. These are daily sports activities or daily work associated with a lot of movement and manual labor, e.g., farming
1.9 - extreme activity. This is more likely for professional athletes and people with active jobs like working with weights, etc.
Your response: """))
            break # Exit the loop on successful indicator input
        except ValueError:
            print("Error: Incorrect indicator value entered. Please re-enter your age.")

    # Calculate the user's daily calorie intake
    calories = calories_intake_per_day(weight, height, age, human_activity_indicator, male_or_female)

    print(f"Your daily calorie intake is: {calories:.2f} calories")

    proteins, fats, carbohydrates = protein_fats_carbohydrates(weight, calories)

    headers = ["Proteins per day", "Fats per day", "Carbohydrates per day", "Calories intake per day"]
    data = [[proteins, fats, carbohydrates, calories]]
    colalign = ("center", "center", "center", "center")
    table = tabulate(data, headers, tablefmt="grid", colalign=colalign)
    print(table)
    print("NOW LETS GO TO THE GYM!!!")