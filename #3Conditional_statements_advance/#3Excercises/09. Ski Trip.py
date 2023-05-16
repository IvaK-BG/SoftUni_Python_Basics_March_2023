number_days = int(input())
type = input()
feedback = input()

discount = 0
room_for_one_person = 18
apartament = 25
president_apartment = 35
total = 0

if type == "room for one person":
    if number_days < 10:
        total = number_days * 18
    elif type == "apartment":
        discount *= 0.70
    total = number_days * 25 * discount
    elif type == "president apartment":
        discount *= 0.90
        total = 35 * number_days * discount


elif 10 < number_days <= 15:
    if type == "room for one person":
        total = number_days * room_for_one_person
    elif type == "apartment":
        discount *= 0.65
        total = number_days * apartament * discount
    elif type == "president apartment":
        discount *= 0.85
        total = president_apartment * number_days * discount
elif number_days > 15:
    if type == "room for one person":
        total = number_days * room_for_one_person
    elif type == "apartment":
        discount *= 0.50
        total = number_days * apartament * discount
    elif type == "president apartment":
        discount *= 0.80
        total = president_apartment * number_days * discount

if feedback == "positive":
    total = total + (total * 0.25)
else:
    total = total - (total * 0.10)

print(f"{total:.2f}")

