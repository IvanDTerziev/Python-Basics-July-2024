budget = float(input())
statists = int(input())
clothes_price = float(input())

decor = budget * 0.10
clothes = statists * clothes_price

if statists > 150:
    clothes *= 0.90

total_sum = decor + clothes

if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - budget:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_sum:.2f} leva left.")
