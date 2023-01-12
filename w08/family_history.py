# Colors
red_color = '\033[0;31m'
green_color = '\033[0;32m'
yellow_color = '\033[0;33m'
blue_color = '\033[0;34m'
purple_color = '\033[0;35m'
cyan_color = '\033[0;36m'
gray_color = '\033[1;30m'
end_color = '\033[0m'

# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    print()

    count_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print(f'\n----------------------------------------------------------------------------------------')
    print(f'|{"":<10}{green_color}NAME{end_color}{"":<10}|{end_color}{"":<5}{green_color}BIRTH YEAR{end_color}{"":<5}|{"":<5}{green_color}DEATH YEAR{end_color}{"":<5}|{"":<5}{green_color}DEATH AGE{end_color}{"":<5}|')
    print(f'----------------------------------------------------------------------------------------')
    for key, value in people_dict.items():
        age_death = value[DEATH_YEAR_INDEX] - value[BIRTH_YEAR_INDEX]
        print(
            f'| {blue_color}{value[NAME_INDEX]:<23}{end_color}|{"":<8}{red_color}{value[BIRTH_YEAR_INDEX]:<12}{end_color}|{"":<8}{red_color}{value[DEATH_YEAR_INDEX]:<12}{end_color}|{"":<9}{red_color}{age_death:<10}{end_color}|')
    print(f'----------------------------------------------------------------------------------------')


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    males = 0
    females = 0
    for key, value in people_dict.items():
        if value[GENDER_INDEX] == 'M':
            males += 1
        else:
            females += 1

    print(f'{yellow_color}¬{end_color} Number of males: {green_color}{males}{end_color}\n{yellow_color}¬{end_color} Number of females: {green_color}{females}{end_color}')


def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print(f'|--------------------------------------------------------------|')
    print(f'|{"":<26}{red_color}MARRIAGES{end_color}{"":<26} |')
    print(f'|--------------------------------------------------------------|')
    for key, value in marriages_dict.items():
        wedding_year = value[WEDDING_YEAR_INDEX]
        husband = people_dict[value[HUSBAND_KEY_INDEX]]
        wife = people_dict[value[WIFE_KEY_INDEX]]
        husband_age = value[WEDDING_YEAR_INDEX] - husband[BIRTH_YEAR_INDEX]
        wife_age = value[WEDDING_YEAR_INDEX] - wife[BIRTH_YEAR_INDEX]
        print(f'| {husband[NAME_INDEX]:<20} | {husband_age} | {wedding_year} | {wife[NAME_INDEX]:<20} | {wife_age} |')
    print(f'|--------------------------------------------------------------|')


def count_marriages(marriages_dict, people_dict):
    """Count and print the number of marriages that each person had in his or her lifetime.

    Parameters:
        marriages_dict: a list of marriages.
        people_dict: a list of people.
    Return: nothing
    """
    people_married = {}
    for key, value in marriages_dict.items():
        husband = value[HUSBAND_KEY_INDEX]
        wife = value[WIFE_KEY_INDEX]
        if husband in people_married:
            people_married[husband] += 1
        else:
            people_married[husband] = 1

        if wife in people_married:
            people_married[wife] += 1
        else:
            people_married[wife] = 1

    print(f'{red_color}Times married{end_color}')
    for key, value in people_married.items():
        print(f'{people_dict[key][NAME_INDEX]:<18} {people_married[key]}')

    most_times = ['', 0]
    for key, value in people_married.items():
        if value > most_times[1]:
            most_times[0] = key
            most_times[1] = value
    print(
        f'\n{red_color}[!]{end_color} {people_dict[most_times[0]][NAME_INDEX]} married {red_color}{most_times[1]}{end_color} times\n')

    # If this file was executed like this:
    # > python teach_solution.py
    # then call the main function. However, if this file
    # was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
