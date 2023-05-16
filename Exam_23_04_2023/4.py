from math import ceil

days = int(input())
first_day = float(input())
total_km = first_day

for i in range(days):
    percent = int(input())
    daily_increase = first_day * percent / 100
    first_day += daily_increase
    total_km += first_day

if total_km >= 1000:
    print(f"You've done a great job running {ceil(total_km - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_km)} more kilometers")

