w = float(input())
h = float(input())

w_to_cm = w * 100
h_to_cm = h * 100

rows = w_to_cm // 120
h_to_cm -= 100

buros_in_row = h_to_cm // 70

buros_all = rows * buros_in_row - 3

print(buros_all)