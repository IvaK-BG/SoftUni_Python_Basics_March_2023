movie = input()
r = int(input())
c = int(input())

income = 0

cinema_capacity = r * c

if movie == "Premiere":
    income = cinema_capacity * 12
elif movie == "Normal":
    income = cinema_capacity * 7.5
elif movie =="Discount":
    income = cinema_capacity * 5

print(f"{income:.2f}")