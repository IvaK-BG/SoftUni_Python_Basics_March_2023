number_juniors = int(input())
number_seniors = int(input())
trace = input()

junior_trail = 5.5
junior_cross_country = 8
junior_downhill = 12.25
junior_road = 20
senior_trail = 7
senior_cross_country = 9.5
senior_downhill = 13.75
senior_road = 21.50



junior_total = 0
price_senior = 0
total_cyclists = number_juniors + number_seniors
total = 0

if trace == "cross-country" and total_cyclists >= 50:
    junior_total = (number_juniors * junior_cross_country) - 0.25 * (number_juniors * junior_cross_country)
    senior_total = (number_seniors * senior_cross_country) - 0.25 * (number_seniors * senior_cross_country)
    total = (junior_total + senior_total) - 0.05 * (junior_total + senior_total)
else:
    total =  ((number_juniors * junior_cross_country) + (number_seniors * senior_cross_country)) - 0.05 * \
             ((number_juniors * junior_cross_country) + (number_seniors * senior_cross_country))

if trace == "trail":
    junior_total = number_juniors * junior_trail
    senior_total = number_seniors * senior_trail
    total = (junior_total + senior_total) - (junior_total + senior_total) * 0.05
elif trace == "downhill":
    junior_total = number_juniors * junior_downhill
    senior_total = number_seniors * senior_downhill
    total = (junior_total + senior_total) - (junior_total + senior_total) * 0.05
elif trace == "road":
    junior_total = number_juniors * junior_road
    senior_total = number_seniors * senior_road
    total = (junior_total + senior_total) - (junior_total + senior_total) * 0.05



print(f"{total:.2f}")
