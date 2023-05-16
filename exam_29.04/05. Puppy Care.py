zakupena_hrana_kg = int(input())
zakupena_hrana_gr = zakupena_hrana_kg * 1000
total_hrana = 0
command = input()

while command != "Adopted":
    hrana_grama = int(command)
    total_hrana += hrana_grama
    command = input()

if total_hrana <= zakupena_hrana_gr:
    print(f"Food is enough! Leftovers: {zakupena_hrana_gr - total_hrana} grams.")
else:
    print(f"Food is not enough. You need {abs(total_hrana - zakupena_hrana_gr)} grams more.")


