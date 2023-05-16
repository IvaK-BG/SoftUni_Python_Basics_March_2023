start_meters = 5364
total_meters = 0
count_days = 1

while True:
    command = input()

    if command == "END" or count_days > 5 or total_meters == 8848:
        break
    print(f"Goal reached for {count_days} days!")


    meters_climbed = int(command)

    if command == "Yes":
        total_meters = 0
        count_days += 1
    else:
        total_meters += meters_climbed
        count_days += 1
total = start_meters + total_meters

if total_meters < 8848 or count_days > 5:
    print("Failed!")
    print(f"{total}")










