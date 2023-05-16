budget = float(input())
season = input()

if budget <= 100 and season == "Summer":
        price = 0.35 * budget
        print("Economy class")
        print(f"Cabrio - {price:.2f}")

elif season == "Winter" and budget <= 100:
        price = 0.65 * budget
        print(f"Economy class")
        print(f"Jeep - {price:.2f}")
elif 100 < budget <= 500 and season == "Summer":
        price = 0.45 * budget
        print("Compact class")
        print(f"Cabrio - {price:.2f}")
elif season == "Winter" and 100 < budget <= 500:
        price = 0.80 * budget
        print("Compact class")
        print(f"Jeep - {price:.2f}")
elif budget > 500:
    price = 0.90 * budget
    print(f"Luxury class")
    print(f"Jeep - {price:.2f}")












