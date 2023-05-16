n = int(input())
total_sum = 0
diff = 0

for i in range (0, n):
    current_number = int(input())
    total_sum += current_number

diff = total_sum / n

print(f"{diff:.2f}")