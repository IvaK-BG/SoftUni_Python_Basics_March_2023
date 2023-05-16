count_months = int(input())
water = 20
internet = 15
other_bills = 0
electricity_bill = 0
bills_count = 0


for _ in range(1, count_months + 1):
    electricity_bill_mount = float(input())
    electricity_bill += electricity_bill_mount
    other_bills += (electricity_bill_mount + water + internet) + 0.20 * (electricity_bill_mount + water + internet)
    bills_count += 1

internet = internet * count_months
water = water * count_months
average_bills = (electricity_bill + internet + water + other_bills) / count_months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average_bills:.2f} lv")



