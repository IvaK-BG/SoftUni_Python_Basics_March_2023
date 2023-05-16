season = input()
km_per_month = float(input())

total = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        total = (km_per_month * 0.75) * 4
    elif season == "Summer":
        total = (km_per_month * 0.90) * 4
    elif season == "Winter":
        total = (km_per_month * 1.05) * 4
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        total = (km_per_month * 0.95) * 4
    elif season == "Summer":
        total = (km_per_month * 1.1) * 4
    elif season == "Winter":
        total = (km_per_month * 1.25) * 4
elif 10000 < km_per_month <= 20000:
    if season == "Spring" or season == "Autumn" or season == "Winter" or season == "Summer":
        total = km_per_month * 1.45 * 4

tax = 0.10 * total
diff = total - tax

print(f"{diff:.2f}")

