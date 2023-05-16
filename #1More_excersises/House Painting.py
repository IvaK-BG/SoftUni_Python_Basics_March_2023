x = float(input())
y = float(input())
h = float(input())

area_side_walls = y * x
area_windows = 1.5 * 1.5
total_area_side_walls = (2 * area_side_walls) - (area_windows * 2)

area_front_wall = x * x
sum_area_front_wall = 2 * area_front_wall - (1.2 * 2)

total_area = total_area_side_walls + sum_area_front_wall
needed_color = total_area / 3.4



area_big_roof = (x * y) * 2
area_triangle_roof = 2 * (x * h / 2)
roof_total_area = area_big_roof + area_triangle_roof
needed_color_roof = roof_total_area / 4.3

print(f"{needed_color:.2f}")
print(f"{needed_color_roof:.2f}")