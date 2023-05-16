import math
days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

dog_needed_food = dog_food_kg * days
cat_needed_food = cat_food_kg * days
turtle_needed_food = turtle_food_gr * days / 1000

total_need_food = dog_needed_food + cat_needed_food + turtle_needed_food

diff = abs(food_kg - total_need_food)

if total_need_food <= food_kg:
    print(f"{math.floor(diff)} kilos of food left.")

else:
    diff > total_need_food
    print(f"{math.ceil(diff)} more kilos of food are needed.")


