from math import ceil
name_serial = str(input())
movie_lenght = int(input())
break_lenght = int(input())

lunch_lenght = break_lenght * 1 / 8
rest_lenght = break_lenght * 1 / 4

time_left = break_lenght - lunch_lenght - rest_lenght

if movie_lenght <= time_left:
    time_left = time_left - movie_lenght
    print(f"You have enough time to watch {name_serial} and left with {ceil(time_left)} minutes free time.")
else:
    time_left = movie_lenght - time_left
    print(f"You don't have enough time to watch {name_serial}, you need {ceil(time_left)} more minutes.")

