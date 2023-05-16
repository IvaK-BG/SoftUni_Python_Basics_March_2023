season = input()
group_type = input()
number_students = int(input())
nights_count = int(input())

if season == "Winter":
    if group_type == "girls":
        price = 9.6
        sport = "Gymnastics"
    elif group_type == "boys":
        price = 9.6
        sport = "Judo"
    elif group_type == "mixed":
        price = 10
        sport = "Ski"
if season == "Spring":
    if group_type == "girls":
        price = 7.2
        sport = "Athletics"
    elif group_type == "boys":
        price = 7.2
        sport = "Tennis"
    elif group_type == "mixed":
        price = 9.5
        sport = "Cycling"
if season == "Summer":
    if group_type == "girls":
        price = 15
        sport = "Volleyball"
    elif group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "mixed":
        price = 20
        sport = "Swimming"
total = number_students * nights_count * price

if number_students >= 50:
    total *= 0.5
elif 20 <= number_students < 50:
    total *= 0.85
elif 10 <= number_students < 20:
    total *= 0.95


print(f"{sport} {total:.2f} lv.")