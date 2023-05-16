budget = float(input())
number_graphics = int(input())
number_processors = int(input())
number_ram = int(input())

graphics_sum = number_graphics * 250
processors_price = 0.35 * graphics_sum
ram_price = 0.10 * graphics_sum
processors_sum = processors_price * number_processors
ram_sum = ram_price * number_ram

total_sum = graphics_sum + processors_sum + ram_sum

if number_graphics > number_processors:
    total_sum = total_sum - (total_sum * 0.15)

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")