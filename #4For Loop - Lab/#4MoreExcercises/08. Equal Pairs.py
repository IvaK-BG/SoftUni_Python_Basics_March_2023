count = int(input())
previous_sum = int(input()) + int(input())
max_difference = 0

for i in range(count - 1):
    current_sum = int(input()) + int(input())
    max_difference = max(max_difference, abs(previous_sum - current_sum))
    previous_sum = current_sum

if max_difference == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")

