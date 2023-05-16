trip_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_berries = int(input())
number_minions = int(input())
number_trucks = int(input())

order_sum = number_puzzles * 2.6 + number_dolls * 3 + number_berries * 4.1 + number_minions * 8.2 + number_trucks * 2
total_number = number_puzzles + number_dolls + number_minions + number_berries + number_trucks

if total_number >= 50:
    order_sum *= 0.75

rent = order_sum * 0.1

profit = order_sum - rent

diff = abs(profit - trip_price)

if profit >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")





