price_vegetables = float(input())
price_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())
total_sum_in_leva = price_vegetables * total_kg_vegetables + price_fruits * total_kg_fruits
total_sum_in_Eur = total_sum_in_leva / 1.94
print(f"{total_sum_in_Eur:.2f}")