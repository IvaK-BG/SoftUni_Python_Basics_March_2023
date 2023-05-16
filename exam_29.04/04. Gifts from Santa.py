n = int(input())
m = int(input())
s = int(input())

for addresses in range(m, n - 1, - 1):

    if addresses % 2 == 0 and addresses % 3 == 0:
        if addresses != s:
            print(f"{addresses}", end=" ")
        else:
            break
