from datetime import datetime

red_color = '\033[0;31m'
green_color = '\033[0;32m'
yellow_color = '\033[0;33m'
blue_color = '\033[0;34m'
purple_color = '\033[0;35m'
cyan_color = '\033[0;36m'
end_color = '\033[0m'

def calc_tax(sub):
    return sub * 0.06

def calc_total(tax, sub):
    return sub + tax

current_date = datetime.now()
day_week = current_date.weekday()
day_week = 1

print(f'\nxxxxxx {purple_color}DISCOUNT{end_color}{yellow_color}.py{end_color} xxxxxx\n')

discount = 0
subtotal = float(input(f'{purple_color}[+]{end_color} Please enter the subtotal:\n\t{purple_color}-->>{end_color}  '))

if day_week == 1 or day_week == 2:
    if subtotal >= 50:
        discount = subtotal * 0.1
        subtotal -= discount
    else:
        amount_needed = 50 - subtotal
        print(f'\n{red_color}[!]{end_color} You need {green_color}${amount_needed:.2f}{end_color} to receive the discount')
    tax_amount = calc_tax(subtotal)
    total = calc_total(tax_amount, subtotal)
else:
    tax_amount = calc_tax(subtotal)
    total = calc_total(tax_amount, subtotal)

if discount != 0:
    print(f'\n{green_color}[!]{end_color} Discount amount: {green_color}${discount:.2f}{end_color}')
print(f'{red_color}[-]{end_color} Sales tax amount: {red_color}${tax_amount:.2f}{end_color}')
print(f'\nTotal: {purple_color}${total:.2f}{end_color}\n')