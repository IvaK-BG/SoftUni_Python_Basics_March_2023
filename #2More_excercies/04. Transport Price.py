n_km = int(input())
day_night = input()

taxi_start_tax = 0.70
day_tax_km = 0.79
night_tax_km = 0.90
bus_day_night = 0.09
train_day_night = 0.06
bus_min_distance = 20
train_min_distance = 100
total = 0

taxi_day_distance = n_km * 0.79
taxi_night_distance = n_km * 0.90

if n_km < 20:
    if day_night == "day":
        total = taxi_start_tax + n_km * day_tax_km
    else:
        total = taxi_start_tax + n_km * night_tax_km

elif n_km < 100:
     total = n_km * bus_day_night
elif n_km >= 100:
     total = n_km * train_day_night

print(f"{total:.2f}")






