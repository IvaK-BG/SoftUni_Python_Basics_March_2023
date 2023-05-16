from math import floor

poroda_cat = input()
gender = input()
cat_years = 0

if gender == "m":
    if poroda_cat == "British Shorthair":
        cat_years = 13
    elif poroda_cat == "Siamese":
        cat_years = 15
    elif poroda_cat == "Persian":
        cat_years = 14
    elif poroda_cat == "Ragdoll":
        cat_years = 16
    elif poroda_cat == "American Shorthair":
        cat_years = 12
    elif poroda_cat == "Siberian":
        cat_years = 11
    else:
        print(f"{poroda_cat} is invalid cat!")
elif gender == "f":
    if poroda_cat == "British Shorthair":
        cat_years = 14
    elif poroda_cat == "Siamese":
        cat_years = 16
    elif poroda_cat == "Persian":
        cat_years = 15
    elif poroda_cat == "Ragdoll":
        cat_years = 17
    elif poroda_cat == "American Shorthair":
        cat_years = 13
    elif poroda_cat == "Siberian":
        cat_years = 12
    else:
        print(f"{poroda_cat} is invalid cat!")

human_months = cat_years * 12
cat_months = human_months / 6
if cat_months > 0:

    print(f"{floor(cat_months)} cat months")

