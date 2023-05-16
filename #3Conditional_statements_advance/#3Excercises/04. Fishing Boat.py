budget = int(input())
season = (input())
fisher_men_number = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if fisher_men_number <= 6:
    rent *= 0.9
elif 7 <= fisher_men_number <= 11:
    rent *= 0.85
elif fisher_men_number >= 12:
    rent *= 0.75

if fisher_men_number % 2 == 0 and season != "Autumn":
    rent *= 0.95

diff = abs(budget - rent)

if budget < rent:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")