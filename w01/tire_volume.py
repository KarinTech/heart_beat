# Colors
red_color = '\033[0;31m'
green_color = '\033[0;32m'
yellow_color = '\033[0;33m'
end_color = '\033[0m'

import math

print(f'\n|------------------------------|')
print(f'|          {green_color}TIRE VOLUME{end_color}         |')
print(f'|------------------------------|\n')

width = int(input(f'{yellow_color}[+]{end_color} Enter the width of the tire in mm:\n\t{yellow_color}-->>{end_color}  '))
aspect_ratio = int(input(f'\n{yellow_color}[+]{end_color} Enter the aspect ratio of the tire:\n\t{yellow_color}-->>{end_color}  '))
diameter = int(input(f'\n{yellow_color}[+]{end_color} Enter the diameter of the wheel in inches:\n\t{yellow_color}-->>{end_color}  '))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f'\n{red_color}[!]{end_color} The approximate volume is {red_color}{volume:.2f}{end_color} liters\n')