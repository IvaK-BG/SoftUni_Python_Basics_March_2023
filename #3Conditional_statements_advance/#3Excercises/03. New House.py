type_of_flower = input()
number_flower = int(input())
budget = int(input())

sum_flowwer = type_of_flower * number_flower

price = 0
discount = 0

if type_of_flower == "Roses":
    price = 5
    if number_flower > 80:
        discount += 0.1
elif type_of_flower == "Dahlias":
    price = 3.8
    if number_flower > 90:
        discount += 0.15
elif type_of_flower == "Tulips":
    price = 2.8
    if number_flower > 80:
        discount += 0.15
elif type_of_flower == "Narcissus":
    price = 3
    if number_flower < 120:
        discount -= 0.15
elif type_of_flower == "Gladiolus":
    price = 2.5
    if number_flower < 80:
        discount -= 0.20

total_price = number_flower * price * (1 - discount)

diff = abs(budget - total_price)

if budget < total_price:
    print(f"Not enough money, you need {diff:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {number_flower} {type_of_flower} and {diff:.2f} leva left.")

