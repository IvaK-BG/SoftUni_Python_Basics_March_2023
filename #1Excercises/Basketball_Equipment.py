price_of_year_basketball = int(input())
price_of_shoes = price_of_year_basketball - (price_of_year_basketball * 0.4)
basketball_kit = price_of_shoes - (price_of_shoes * 0.2)
basketball_ball = 1/4 * basketball_kit
basketball_accs = 1/5 * basketball_ball
total_price = price_of_year_basketball + price_of_shoes + basketball_kit + basketball_ball + basketball_accs
print(total_price)
