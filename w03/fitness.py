from datetime import datetime

purple_color = '\033[0;35m'
cyan_color = '\033[0;36m'
end_color = '\033[0m'

print(
    f'\n         {cyan_color}/{end_color} ------- {cyan_color}\{end_color}         ')
print(f'{cyan_color}H{end_color} ------   {purple_color}FITNESS{end_color}   ------ {cyan_color}H{end_color}')
print(
    f'         {cyan_color}\{end_color} ------- {cyan_color}/{end_color}         ')


def main():
    gender = input(
        f'\n{purple_color}[+]{end_color} Please enter your gender {cyan_color}(M or F){end_color}:\n\t{purple_color}-->>{end_color}  ')
    birthdate = input(
        f'\n{purple_color}[+]{end_color} Enter your birthdate {cyan_color}(YYYY-MM-DD){end_color}:\n\t{purple_color}-->>{end_color}  ')
    weight = float(
        input(f'\n{purple_color}[+]{end_color} Enter your weight in U.S. pounds:\n\t{purple_color}-->>{end_color}  '))
    height = float(
        input(f'\n{purple_color}[+]{end_color} Enter your height in U.S. inches:\n\t{purple_color}-->>{end_color}  '))
    age = compute_age(birthdate)
    weight_kg = kg_from_lb(weight)
    height_cm = cm_from_in(height)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)
    print(f'\n{cyan_color}¬{end_color} Age (years): {cyan_color}{age}{end_color}')
    print(f'{cyan_color}¬{end_color} Weight (kg): {cyan_color}{weight_kg:.2f}{end_color}')
    print(f'{cyan_color}¬{end_color} Height (cm): {cyan_color}{height_cm}{end_color}')
    print(f'{cyan_color}¬{end_color} Body mass index: {cyan_color}{bmi}{end_color}')
    print(f'{cyan_color}¬{end_color} Basal metabolic rate (kcal/day): {cyan_color}{bmr}{end_color}\n')
    return


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and
            birthdate.day > today.day):
        years -= 1
    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return round(pounds * 0.45359237, 2)


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return round(inches * 2.54, 1)


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return round((10000 * weight) / (height**2), 1)


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    bmr = None
    if gender.lower() == 'm':
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif gender.lower() == 'f':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    return round(bmr)


main()

print(
    f'         {cyan_color}/{end_color} ------- {cyan_color}\{end_color}         ')
print(f'{cyan_color}H{end_color} ------   {purple_color}  BYE  {end_color}   ------ {cyan_color}H{end_color}')
print(
    f'         {cyan_color}\{end_color} ------- {cyan_color}/{end_color}         \n')
