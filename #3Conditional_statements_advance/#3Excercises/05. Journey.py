budget = float(input())
season = input()
destination = ""
price = 0
type = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = 0.30 * budget
        type = "Camp"
    elif season == "winter":
        price = 0.70 * budget
        type = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = 0.40 * budget
        type = "Camp"
    elif season == "winter":
        price = 0.80 * budget
        type = "Hotel"
else:
    destination = "Europe"
    price = 0.90 * budget
    type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type} - {price:.2f}")






