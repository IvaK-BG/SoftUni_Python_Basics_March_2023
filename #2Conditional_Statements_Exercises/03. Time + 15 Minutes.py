curr_h = int(input())
curr_m = int(input())

total_time_m = curr_h * 60 + curr_m + 15

hours = total_time_m // 60
minutes = total_time_m % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")



