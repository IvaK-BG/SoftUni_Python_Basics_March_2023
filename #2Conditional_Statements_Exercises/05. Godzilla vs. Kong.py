budget_movie = float(input())
number_statists = int(input())
price_per_statists = float(input())

sum_decor = 0.1 * budget_movie
sum_clothes_statists = number_statists * price_per_statists

if number_statists > 150:
    sum_clothes_statists *= 0.90

total_movie_sum = sum_decor + sum_clothes_statists


diff = abs(budget_movie - total_movie_sum)

if budget_movie >= total_movie_sum:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
