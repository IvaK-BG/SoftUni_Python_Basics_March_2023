q_nylon = int(input())
q_color = int(input())
q_thinner = int(input())
works_hours = int(input())

sum_nylon = (q_nylon + 2) * 1.50
sum_color = (q_color + (0.1 * q_color)) * 14.50
sum_thinner = q_thinner * 5
total_materials_sum = sum_nylon + sum_color + sum_thinner + 0.40
workers_earn = total_materials_sum * 0.3 * works_hours
total_payment = total_materials_sum + workers_earn
print(total_payment)