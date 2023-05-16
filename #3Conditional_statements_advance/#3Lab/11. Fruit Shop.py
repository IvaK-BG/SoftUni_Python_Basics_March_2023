fruit = input()
day_of_week = input()
q = float(input())
total = 0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or \
    day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        total = q * 2.5
    elif fruit == "apple":
        total = q * 1.2
    elif fruit == "orange":
        total = q * 0.85
    elif fruit == "grapefruit":
        total = q * 1.45
    elif fruit == "kiwi":
        total = q * 2.70
    elif fruit == "pineapple":
        total = q * 5.5
    elif fruit == "grapes":
        total = q * 3.85


if day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        total = q * 2.7
    elif fruit == "apple":
        total = q * 1.25
    elif fruit == "orange":
        total = q * 0.90
    elif fruit == "grapefruit":
        total = q * 1.60
    elif fruit == "kiwi":
        total = q * 3
    elif fruit == "pineapple":
        total = q * 5.6
    elif fruit == "grapes":
        total = q * 4.2


if (day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or \
    day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday" or day_of_week == "Sunday") \
    and (fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or \
         fruit == "pineapple" or fruit == "grapes"):
    print(f"{total:.2f}")
else:
    print("error")





