budget = float(input())
season = input()

total_price = 0
place = None
destination = None

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        place = "Camp"
        total_price = budget * 0.30
    else:
        place = "Hotel"
        total_price = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        place = "Camp"
        total_price = budget * 0.40
    else:
        place = "Hotel"
        total_price = budget * 0.80

else:
    destination = "Europe"

    place = "Hotel"
    total_price = budget * 0.90


print(f"Somewhere in {destination}")
print(f"{place} - {total_price:.2f}")
