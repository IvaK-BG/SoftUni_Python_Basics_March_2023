open_tabs = int(input())
salary = int(input())

for tab in range(open_tabs):
    current_tabs = input()
    if current_tabs == "Facebook":
        salary -= 150
    elif current_tabs == "Instagram":
        salary -= 100
    elif current_tabs == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)