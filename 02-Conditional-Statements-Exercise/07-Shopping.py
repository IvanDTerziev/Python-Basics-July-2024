budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_sum = video_cards_count * 250
processor_price = 0.35 * video_cards_sum
ram_price = 0.10 * video_cards_sum

total_sum = video_cards_sum + processors_count * processor_price + ram_count * ram_price

discount = 0
if video_cards_count > processors_count:
    discount = 0.15

total_price_with_discount = total_sum * (1 - discount)

if budget >= total_price_with_discount:
    print(f"You have {budget - total_price_with_discount:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price_with_discount - budget:.2f} leva more!")
