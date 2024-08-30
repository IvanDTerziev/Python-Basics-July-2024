ROSES_PRICE = 5.00
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3.00
GLADIOLUS_PRICE = 2.50

type_of_flower = input()
flower_count = int(input())
budget = int(input())

total_price = 0

if type_of_flower == "Roses":
    total_price = flower_count * ROSES_PRICE
elif type_of_flower == "Dahlias":
    total_price = flower_count * DAHLIAS_PRICE
elif type_of_flower == "Tulips":
    total_price = flower_count * TULIPS_PRICE
elif type_of_flower == "Narcissus":
    total_price = flower_count * NARCISSUS_PRICE
elif type_of_flower == "Gladiolus":
    total_price = flower_count * GLADIOLUS_PRICE

if type_of_flower == "Roses" and flower_count > 80:
    total_price *= 0.9
elif type_of_flower == "Dahlias" and flower_count > 90:
    total_price *= 0.85
elif type_of_flower == "Tulips" and flower_count > 80:
    total_price *= 0.85
elif type_of_flower == "Narcissus" and flower_count < 120:
    total_price *= 1.15
elif type_of_flower == "Gladiolus" and flower_count < 80:
    total_price *= 1.2

if total_price <= budget:
    print(f"Hey, you have a great garden with {flower_count} "
          f"{type_of_flower} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
