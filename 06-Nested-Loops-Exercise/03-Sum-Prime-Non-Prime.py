from math import sqrt

sum_primes = 0
sum_non_primes = 0

while True:
    command = input()

    if command == "stop":
        break

    current_number = int(command)

    if current_number < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for num in range(2, int(sqrt(current_number)) + 1):
        if current_number % num == 0:
            is_prime = False
            break

    if is_prime and current_number > 1:
        sum_primes += current_number
    else:
        sum_non_primes += current_number

print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")
