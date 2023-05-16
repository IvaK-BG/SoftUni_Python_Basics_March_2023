starting_letter = input()
ending_letter = input()
skip_letter = input()

counter = 0

for one in range(ord(starting_letter), ord(ending_letter) + 1):
    for two in range(ord(starting_letter), ord(ending_letter) + 1):
        for three in range(ord(starting_letter), ord(ending_letter) + 1):
            combination = chr(one) + chr(two) + chr(three)
            if skip_letter in str(combination):
                continue
            else:
                counter += 1

            print(combination, end=' ')
print(counter)
