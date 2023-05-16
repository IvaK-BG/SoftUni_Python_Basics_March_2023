import math
number_magnolia = int(input())
number_zjumbjuli = int(input())
number_roses = int(input())
number_cactuses = int(input())
price_gift = float(input())

price_magnolia = 3.25
price_zjumbjuli = 4
price_roses = 3.5
price_cactuses = 8
taxes_percent = 0.05

total_price_floweers = (number_magnolia * price_magnolia) + (number_zjumbjuli * price_zjumbjuli) + \
                       (number_roses * price_roses) + (number_cactuses * price_cactuses)
taxes = total_price_floweers * 0.05

profit = total_price_floweers - taxes

diff = abs(profit - price_gift)

if profit >= price_gift:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")