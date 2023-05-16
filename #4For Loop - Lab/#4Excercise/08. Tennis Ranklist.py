tournaments_count = int(input())
points = int(input())
tournament_points = 0
wins = 0
for tournament in range(tournaments_count):
    tournament_score = input()

    if tournament_score == "W":
        tournament_points += 2000
        wins += 1
    elif tournament_score == "F":
        tournament_points += 1200
    elif tournament_score == "SF":
        tournament_points += 720

points += tournament_points

print(f"Final points: {points}")
print(f"Average points: {tournament_points // tournaments_count}")
print(f"{wins / tournaments_count * 100:.2f}%")



