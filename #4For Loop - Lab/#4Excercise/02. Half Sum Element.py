import sys

n = int(input())

sum_numbers = 0
max_num = -sys.maxsize

for i in range (0, n):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_num:
        max_num = current_number

sum_numbers -= max_num

if max_num == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {abs(max_num - sum_numbers)}")

