starting_point = 5364
mountain_top = 8848

day = 1

while True:
    camping = input()
    if day == 5 or starting_point >= mountain_top or camping == 'END':
        break

    meters = int(input())
    if camping == "Yes":
        day += 1

    starting_point += meters

if starting_point < mountain_top:
    print(f"Failed!")
    print(f"{starting_point}")
else:
    print(f"Goal reached for {day} days!")