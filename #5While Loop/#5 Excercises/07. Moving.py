width = int(input())
length = int(input())
height = int(input())
space_volume = width * length * height
number_boxes = 0

while space_volume > 0:
    command = input()
    if command == "Done":
        break
    space_volume -= int(command)

if space_volume > 0:
    print(f"{space_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space_volume)} Cubic meters more.")