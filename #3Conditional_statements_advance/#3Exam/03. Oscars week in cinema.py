name_movie = input()
hall_var = input()
tickets_count = int(input())
price = 0


if name_movie == "A Star Is Born":
    if hall_var == "normal":
        price = tickets_count * 7.5
    elif hall_var == "luxury":
        price = tickets_count * 10.50
    elif hall_var == "ultra luxury":
        price = tickets_count * 13.50

elif name_movie == "Bohemian Rhapsody":
    if hall_var == "normal":
        price = tickets_count * 7.35
    elif hall_var == "luxury":
        price = tickets_count * 9.45
    elif hall_var == "ultra luxury":
        price = tickets_count * 12.75
elif name_movie == "Green Book":
    if hall_var == "normal":
        price = tickets_count * 8.15
    elif hall_var == "luxury":
        price = tickets_count * 10.25
    elif hall_var == "ultra luxury":
        price = tickets_count * 13.25
elif name_movie == "The Favourite":
    if hall_var == "normal":
        price = tickets_count * 8.75
    elif hall_var == "luxury":
        price = tickets_count * 11.55
    elif hall_var == "ultra luxury":
        price = tickets_count * 13.95

print(f"{name_movie} -> {price:.2f} lv.")




