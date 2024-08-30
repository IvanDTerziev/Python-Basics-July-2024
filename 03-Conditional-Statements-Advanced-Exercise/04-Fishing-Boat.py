SPRING_PRICE = 3000
SUMMER_AUTUMN_PRICE = 4200
WINTER_PRICE = 2600

DISCOUNT_6_OR_LESS = 0.10
DISCOUNT_7_TO_11 = 0.15
DISCOUNT_12_OR_MORE = 0.25
ADDITIONAL_DISCOUNT_EVEN_FISHERMEN = 0.05

group_budget = int(input())
season = input()
fishermen = int(input())

total_price = 0

if season == "Spring":
    total_price = SPRING_PRICE
elif season == "Summer" or season == "Autumn":
    total_price = SUMMER_AUTUMN_PRICE
else:
    total_price = WINTER_PRICE

if fishermen <= 6:
    total_price -= total_price * DISCOUNT_6_OR_LESS
elif 7 <= fishermen <= 11:
    total_price -= total_price * DISCOUNT_7_TO_11
else:
    total_price -= total_price * DISCOUNT_12_OR_MORE

if fishermen % 2 == 0 and season != "Autumn":
    total_price -= total_price * ADDITIONAL_DISCOUNT_EVEN_FISHERMEN

if group_budget >= total_price:
    print(f"Yes! You have {group_budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - group_budget:.2f} leva.")
