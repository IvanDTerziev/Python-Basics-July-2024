count_people = int(input())
season = input()

discount = 1
price = 0

if season == "spring":
    if count_people <= 5:
        price = 50
    else:
        price = 48
elif season == "summer":
    if count_people <= 5:
        price = 48.5
    else:
        price = 45
    discount = 0.85
elif season == "autumn":
    if count_people <= 5:
        price = 60
    else:
        price = 49.5
elif season == "winter":
    if count_people <= 5:
        price = 86
    else:
        price = 85
    discount = 1.08
else:
    exit()

total_cost = count_people * price * discount

print(f"{total_cost:.2f} leva.")
