is_prime = True
prime_sum = 0
non_prime_sum = 0

input_line = input()
while input_line != "stop":
    current_number = int(input_line)
    if current_number < 0 :
        print("Number is negative.")
    else:
        for i in range(2, current_number):
            if current_number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += current_number
        else:
            non_prime_sum += current_number
            is_prime = True
    input_line = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")


