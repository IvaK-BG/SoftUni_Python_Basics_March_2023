number_days = int(input())
type_room = input()
feedback = input()

total = 0

if type_room == "room for one person":
    if (number_days < 10) or (10 < number_days <= 15) or (number_days > 15):
        total = number_days * 18

elif type_room == "apartment":
    if number_days < 10:
        total = number_days * 25 * 0.70
    elif 10 < number_days <= 15:
        total = number_days * 25 * 0.65
    else:
        total = number_days * 25 * 0.5

elif type_room == "president apartment":
    if number_days < 10:
        total = number_days * 35 * 0.90
    elif 10 < number_days <= 15:
        total = number_days * 35 * 0.85
    else:
        total = number_days * 35 * 0.8

if feedback == "positive":
    total = total + (total * 0.25)
elif feedback == "negative":
    total = total - (total * 0.10)

print(f"{total:.2f}")

