n1 = int(input())
n2 = int(input())
n3 = int(input())

for num1 in range(1, n1 +1):
    for num2 in range(1, n2 + 1):
        for num3 in range(1, n3 + 1):
            if num1 % 2 == 0 and num3 % 2 == 0 and str(num2) in "2357":
                print(f"{num1} {num2} {num3}")