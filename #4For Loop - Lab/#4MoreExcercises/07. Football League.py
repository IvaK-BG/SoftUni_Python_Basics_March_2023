stadium_capacity = int(input())
count_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0


for _ in range(1, count_fans + 1):
    sector = input()
    if sector == "A":
        fans_a += + 1
    elif sector == "B":
        fans_b += + 1
    elif sector == "V":
        fans_v += + 1
    elif sector == "G":
        fans_g += + 1


fans_a = (fans_a / count_fans) * 100
fans_b = (fans_b / count_fans) * 100
fans_v = (fans_v / count_fans) * 100
fans_g = (fans_g / count_fans) * 100
total_fans = (count_fans / stadium_capacity) * 100

print(f"{fans_a:.2f}%\n{fans_b:.2f}%\n{fans_v:.2f}%\n{fans_g:.2f}%\n{total_fans:.2f}%")




