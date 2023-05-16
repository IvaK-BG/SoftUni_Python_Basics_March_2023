import math
x_sq_m_grape = int(input())
y_grape_per_sq_m = float(input())
z_needed_litres_wine = int(input())
number_workers = int(input())

total_grape = x_sq_m_grape * y_grape_per_sq_m
wine_litres = 0.40 * total_grape / 2.5

over_wine = abs(wine_litres - z_needed_litres_wine)


if wine_litres < z_needed_litres_wine:
    print(f"It will be a tough winter! More {math.floor(over_wine)} liters wine needed.")
else:
    total_grape >= z_needed_litres_wine
    wine_per_worker = over_wine / number_workers
    print(f"Good harvest this year! Total wine: {math.floor(wine_litres)} liters.")
    print(f"{math.ceil(over_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")