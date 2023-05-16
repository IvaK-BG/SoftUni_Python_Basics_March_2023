count_days = int(input())
km_first_day = float(input())
k_norm = 0
distance = 0
total_distance = 0


for days in range(1, count_days + 1):
    percent_increase = int(input())
    if distance == km_first_day:
        total_distance = distance + (distance * percent_increase)



if distance >= 1000:
    print(f"You've done a great job running {abs(distance - 1000):.2f} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {abs(distance - 1000):.2f} more kilometers")


