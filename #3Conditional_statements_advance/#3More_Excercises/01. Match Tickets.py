budget = float(input())
category = input()
number_fans = int(input())

transport = 0
total_tickets_price = 0
diff = 0

if number_fans <= 4:
     transport = 0.75 * budget
elif number_fans <= 9:
    transport = 0.60 * budget
elif number_fans <= 24:
     transport = 0.50 * budget
elif number_fans <= 49:
    transport = 0.40 * budget
elif number_fans >= 50:
    transport = 0.25 * budget

if category == "Normal":
    total_tickets_price = number_fans * 249.99
elif category == "VIP":
    total_tickets_price = number_fans * 499.99

diff = budget - transport - total_tickets_price




if diff < 0:
   print(f"Not enough money! You need {abs(diff):.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")






