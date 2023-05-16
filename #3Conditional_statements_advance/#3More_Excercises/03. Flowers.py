number_hrizantemi = int(input())
number_roses = int(input())
number_laleta = int(input())
season = input()
day_type = input()

price_hrizantemi = 0
price_roses = 0
price_laleta = 0
aranjiment = 2

if season == "Spring" or season == "Summer":
    price_hrizantemi = 2
    price_roses = 4.10
    price_laleta = 2.5
elif season == "Autumn" or season == "Winter":
    price_hrizantemi = 3.75
    price_roses = 4.5
    price_laleta = 4.15

total_flowers = number_hrizantemi + number_roses + number_laleta
bucket = number_hrizantemi * price_hrizantemi + number_roses * price_roses + number_laleta * price_laleta

if day_type == "Y":
    bucket *= 1.15

if number_laleta > 7 and season == "Spring":
    bucket *= 0.95
if number_roses >= 10 and season == "Winter":
    bucket *= 0.90
if total_flowers > 20:
    bucket *= 0.80

print(f"{bucket + aranjiment:.2f} ")
