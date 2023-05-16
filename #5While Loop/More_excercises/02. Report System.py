total_sum_to_be_collected = int(input())
command = input()
payment_type = 0
card_payment = 0
cash_payment = 0
card_count = 0
cash_count = 0

while command != "End":
    payment_type += 1
    product_price = int(command)

    if product_price > 100 and payment_type == 1:
        print("Error in transaction!")
    elif product_price < 10 and payment_type == 2:
        print("Error in transaction!")
    if product_price <= 100 and payment_type == 1:
        cash_payment += product_price
        cash_count += 1
        print("Product sold!")
    elif product_price > 10 and payment_type == 2:
        card_payment += product_price
        card_count += 1
        print("Product sold!")

    total_payment = card_payment + cash_payment
    if total_payment >= total_sum_to_be_collected:
        print(f"Average CS: {cash_payment / cash_count:.2f}")
        print(f"Average CC: {card_payment / card_count:.2f}")
        break

    if payment_type == 2:
        payment_type = 0

    command = input()

else:
    print("Failed to collect required money for charity.")