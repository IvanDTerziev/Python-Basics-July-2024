days = int(input())
type_of_property = input()
rating = input()

number_of_nights = days - 1
costs = 0

if type_of_property == "room for one person":
    costs = 18.00

elif type_of_property == "apartment":
    costs = 25.00
    if number_of_nights < 10:
        costs *= 0.70
    elif number_of_nights <= 15:
        costs *= 0.65
    else:
        costs *= 0.50

elif type_of_property == "president apartment":
    costs = 35.00
    if number_of_nights < 10:
        costs *= 0.90
    elif number_of_nights <= 15:
        costs *= 0.85
    else:
        costs *= 0.80

total_sum = number_of_nights * costs
if rating == "positive":
    total_sum *= 1.25
elif rating == "negative":
    total_sum *= 0.90

print(f"{total_sum:.2f}")
