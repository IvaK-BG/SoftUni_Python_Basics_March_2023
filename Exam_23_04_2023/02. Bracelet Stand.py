pocket_per_day = float(input())
money_for_profit = float(input())
taxes_for_all_period = float(input())
gift_price = float(input())


saved_money = 5 * pocket_per_day
profit_money = money_for_profit * 5
total_money = saved_money + profit_money
money_left = total_money - taxes_for_all_period

if money_left > gift_price:
    print(f"Profit: {money_left} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {abs(money_left - gift_price):.2f} BGN.")
