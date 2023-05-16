from math import floor
record_in_sec = float(input())
distance_in_m = float(input())
time_in_sec_per_m = float(input())

total_time_in_sec = distance_in_m * time_in_sec_per_m
bonus_seconds = floor(distance_in_m / 15) * 12.5
total_time_with_bonus = total_time_in_sec + bonus_seconds


if total_time_with_bonus < record_in_sec:
    print(f" Yes, he succeeded! The new world record is {total_time_with_bonus:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time_with_bonus - record_in_sec:.2f} seconds slower.")