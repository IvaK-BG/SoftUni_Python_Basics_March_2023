money_received = float(input())
live_year = int(input())
total_money_left = money_received
starting_year = 18
expenses_per_year = 12000


for year in range(1800, live_year + 1):
    if year % 2 == 0:
        total_money_left -= expenses_per_year
        starting_year += 1
    else:
        total_money_left -= expenses_per_year + (starting_year * 50)
        starting_year += 1

if total_money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {total_money_left:.2f} dollars left.")
else:
    print(f"He will need {abs(total_money_left):.2f} dollars to survive.")

    