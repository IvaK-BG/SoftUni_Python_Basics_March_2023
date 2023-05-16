chicken_quantity = int(input())
fish_quantity = int(input())
veg_quantity = int(input())

sum_of_chicken = chicken_quantity * 10.35
sum_of_fish = fish_quantity * 12.40
sum_of_veg = veg_quantity * 8.15
total_menu_price = sum_of_chicken + sum_of_fish + sum_of_veg
price_of_dessert = total_menu_price * 0.2
total_price = total_menu_price + price_of_dessert + 2.5
print(total_price)