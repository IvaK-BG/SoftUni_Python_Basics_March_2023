budget = float(input())
season = input()
location = ""
type_place = ""
price = 0

if budget <= 1000:
    type_place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.45 * budget
if 1000 < budget <= 3000:
    type_place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.80 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.60 * budget
if budget > 3000:
    type_place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = 0.90 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.90 * budget

print(f"{location} - {type_place} - {price:.2f}")

