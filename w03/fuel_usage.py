blue_color = '\033[0;34m'
cyan_color = '\033[0;36m'
red_color = '\033[0;31m'
green_color = '\033[0;32m'
end_color = '\033[0m'

print('\n|=|-------------------------|=|')
print(f'|=|     {blue_color}fuel efficiency{end_color}     |=|')
print('|=|-------------------------|=|')


def color_return(value):
    if value < 0:
        return red_color
    else:
        return green_color


def main():
    start = float(
        input(f'\n{cyan_color}[+]{end_color} Enter the first odometer reading (miles):\n\t{cyan_color}-->>{end_color}  '))
    end = float(input(
        f'\n{cyan_color}[+]{end_color} Enter the second odometer reading (miles):\n\t{cyan_color}-->>{end_color}  '))
    fuel_amount = float(
        input(f'\n{cyan_color}[+]{end_color} Enter the amount of fuel used (gallons):\n\t{cyan_color}-->>{end_color}  '))
    mpg = miles_per_gallon(start, end, fuel_amount)
    lp100k = lp100k_from_mpg(mpg)

    color = color_return(mpg)
    print(
        f'\n{blue_color}[!]{end_color} {color}{mpg:.1f}{end_color} miles per gallon')
    color = color_return(lp100k)
    print(
        f'{blue_color}[!]{end_color} {color}{lp100k:.2f}{end_color} liters per 100 kilometers\n')
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    return (end_miles - start_miles) / amount_gallons


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return 235.215 / mpg


main()
