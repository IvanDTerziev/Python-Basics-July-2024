balance = 0

while True:
    inpt = input()

    if inpt == "NoMoreMoney":
        break

    amount = float(inpt)

    if amount < 0:
        print("Invalid operation!")
        break

    balance += amount
    print(f"Increase: {amount:.2f}")

print(f"Total: {balance:.2f}")
