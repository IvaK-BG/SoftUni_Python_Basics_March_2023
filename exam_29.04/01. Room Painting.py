import math
count_color = int(input())
count_tapeti = int(input())
gloves_price = float(input())
brush_price = float(input())

total_color_price = count_color * 21.50
total_tapeti_color = count_tapeti * 5.2
needed_gloves = math.ceil(0.35 * count_tapeti)
needed_brushes = math.floor(0.48 * count_color)
total_gloves_price = needed_gloves * gloves_price
total_brushes_price = needed_brushes * brush_price
total = total_color_price + total_tapeti_color + total_gloves_price + total_brushes_price
total_price = 1/15 * total
print(f"This delivery will cost {total_price:.2f} lv.")