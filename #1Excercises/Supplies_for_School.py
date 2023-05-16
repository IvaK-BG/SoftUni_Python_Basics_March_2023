count_of_pens = int(input())
count_of_markers = int(input())
liters_of_preparat = int(input())
percent_of_discount = int(input())
total_price_of_pens = count_of_pens * 5.8
total_price_of_markers = count_of_markers * 7.2
total_price_of_cleaner = liters_of_preparat * 1.2
total_price = total_price_of_pens + total_price_of_markers + total_price_of_cleaner
discount = 0.25 * total_price
final_price = total_price - discount
print(final_price)