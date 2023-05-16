count_moves = int(input())
from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0
invalid = 0
total_points = 0

for _ in range(1, count_moves + 1):
    number = int(input())

    if 0 > number or number > 50:
        invalid += 1
        total_points = total_points / 2

    elif number < 10:
        from_0_9 += 1
        total_points += + (0.20 * number)

    elif number < 20:
        from_10_19 += 1
        total_points += + (0.30 * number)

    elif number < 30:
        from_20_29 += 1
        total_points += + (0.40 * number)

    elif number < 40:
        from_30_39 += 1
        total_points += + 50

    elif number <= 50:
        from_40_50 += 1
        total_points += + 100

invalid = (invalid / count_moves) * 100
from_0_9 = (from_0_9 / count_moves) * 100
from_10_19 = (from_10_19 / count_moves) * 100
from_20_29 = (from_20_29 / count_moves) * 100
from_30_39 = (from_30_39 / count_moves) * 100
from_40_50 = (from_40_50 / count_moves) * 100

print(f"{total_points:.2f}")
print(f"From 0 to 9: {from_0_9:.2f}%")
print(f"From 10 to 19: {from_10_19:.2f}%")
print(f"From 20 to 29: {from_20_29:.2f}%")
print(f"From 30 to 39: {from_30_39:.2f}%")
print(f"From 40 to 50: {from_40_50:.2f}%")
print(f"Invalid numbers: {invalid:.2f}%")

