degree = int(input())
type_of_day = input()

outfit = ""
shoes = ""

if type_of_day == "Morning":
    if 10 <= degree <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degree <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degree >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif type_of_day == "Afternoon":
    if 10 <= degree <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degree <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degree >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif type_of_day == "Evening":
    if 10 <= degree <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degree <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degree >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
