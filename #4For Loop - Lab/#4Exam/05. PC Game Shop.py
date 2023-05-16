count_sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for n in range (1, count_sold_games + 1):
    name_game = input()

    if name_game == "Hearthstone":
        hearthstone += 1
    elif name_game == "Fornite":
        fornite += 1
    elif name_game == "Overwatch":
        overwatch += 1


hearthstone = (hearthstone / count_sold_games) * 100
fornite = (fornite / count_sold_games) * 100
overwatch = (overwatch / count_sold_games) * 100
others = 100 - (hearthstone + fornite + overwatch)

print(f"Hearthstone - {hearthstone:.2f}%")
print(f"Fornite - {fornite:.2f}%")
print(f"Overwatch - {overwatch:.2f}%")
print(f"Others - {others:.2f}%")


