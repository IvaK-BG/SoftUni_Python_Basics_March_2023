n = int(input())
sum = 0
is_number_found = False
for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(0, 9):
            for d in range(9, c, -1):
                if(a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    is_number_found = True
                elif (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_number_found = True
                    break
            if is_number_found:
                break
        if is_number_found:
            break
    if is_number_found:
        break
