vero = int(input()) * 750
plates = 0
pots = 0
vero_needed = 0
counter = 0
command = input()
while command != "End":
    dishes = int(command)
    if dishes == int(command):
        counter += 1
    if counter % 3 == 0:
        pots += dishes
        vero_needed += dishes * 15
    else:
        plates += dishes
        vero_needed += dishes * 5
    if vero_needed > vero:
        break

    command = input()

diff = abs(vero_needed - vero)

if vero_needed <= vero:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")






