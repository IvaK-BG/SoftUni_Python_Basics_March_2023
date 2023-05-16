month = input()
number_nights = int(input())


price_ap = 0
price_studio = 0
discount_studio = 1
discount_apartament = 1



if month == "May" or month == "October":
    price_studio = 50
    price_ap = 65
    if 7 < number_nights <= 14:
        discount_studio *= 0.95

    elif number_nights > 14:
        discount_studio *= 0.7
elif month == "June" or month == "September":
    price_studio = 75.2
    price_ap = 68.7
    if number_nights > 14:
        discount_studio *= 0.8
elif month == "July" or month == "August":
    price_studio = 76
    price_ap = 77

if number_nights > 14:
    discount_apartament *= 0.90

total_price_studio = price_studio * number_nights * discount_studio
total_price_ap = price_ap * number_nights * discount_apartament

print(f"Apartment: {total_price_ap:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
