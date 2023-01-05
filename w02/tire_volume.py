# Colors
red_color = '\033[0;31m'
green_color = '\033[0;32m'
yellow_color = '\033[0;33m'
end_color = '\033[0m'

import math
from datetime import datetime

def save_data(date, width, ratio, diameter, volume, phone='-'):
    with open('volumes.txt', 'at') as volumes:
        print(f'Date: {date:%Y-%m-%d}, Width: {width}, Aspect ratio: {ratio}, Diameter: {diameter}, Volume: {volume}, Phone: {phone}', file=volumes)

print(f'\n|------------------------------|')
print(f'|          {green_color}TIRE VOLUME{end_color}         |')
print(f'|------------------------------|\n')

width = int(input(f'{yellow_color}[+]{end_color} Enter the width of the tire in mm:\n\t{yellow_color}-->>{end_color}  '))
aspect_ratio = int(input(f'\n{yellow_color}[+]{end_color} Enter the aspect ratio of the tire:\n\t{yellow_color}-->>{end_color}  '))
diameter = int(input(f'\n{yellow_color}[+]{end_color} Enter the diameter of the wheel in inches:\n\t{yellow_color}-->>{end_color}  '))

volume = round((math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000, 2)

current_date = datetime.now()

print(f'\n{red_color}[!]{end_color} The approximate volume is {red_color}{volume}{end_color} liters\n')

buy_tires = 0
while buy_tires != 1 and buy_tires != 2:
    buy_tires = int(input(f'{yellow_color}[?]{end_color} Do you want to buy some tires with the dimensions you entered?\n\n{green_color}[1]{end_color} YES\n{red_color}[2]{end_color} NO\n\t{yellow_color}-->>{end_color}  '))
    if(buy_tires == 1):
        phone = input(f'\n{yellow_color}[+]{end_color} Enter your phone number, please\n\t{yellow_color}-->>{end_color}  ')
        save_data(current_date, width, aspect_ratio, diameter, volume, phone)
    else:
        save_data(current_date, width, aspect_ratio, diameter, volume)

print(f'\n|------------------------------|')
print(f'|              {green_color}BYE{end_color}             |')
print(f'|------------------------------|\n')