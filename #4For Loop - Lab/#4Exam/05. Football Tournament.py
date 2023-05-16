club = input()
count_matches = int(input())
win_p = 0
draw_p = 0
l_p = 0
total_points = 0

for number_matches in range(1, count_matches + 1):
    result = input()

    if result == "W":
        win_p += 3
    elif result == "D":
        draw_p += 1
    elif result == "L":
        l_p = 0

if count_matches == 0:
    print(f"{club} hasn't played any games during this season.")

total_points = win_p + draw_p + l_p
win_percent = (win_p / count_matches) * 100

print(f"{club} has won {total_points} points during this season")
print("Total stats:")
print(f"## W: {win_p:.2f}")
print(f"## D: {draw_p}")
print(f"## L: {l_p}")
print(f"Win rate: {win_percent:.2f}%")