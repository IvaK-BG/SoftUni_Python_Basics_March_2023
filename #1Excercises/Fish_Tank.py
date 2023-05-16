length = int(input())
width = int(input())
heigth = int(input())
percent = float(input()) / 100

volume = length * width * heigth
volume_in_liters = volume * 0.001
water_percent = 1 - percent
water_needed = volume_in_liters * water_percent
print(water_needed)