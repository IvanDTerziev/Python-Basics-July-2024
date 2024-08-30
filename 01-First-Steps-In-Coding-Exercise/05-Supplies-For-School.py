pens_nums = int(input())
markers_nums = int(input())
liters = int(input())
discount_percent = int(input())

pens_price = pens_nums * 5.80
markers_price = markers_nums * 7.20
liters_price = liters * 1.20

total_price = pens_price + markers_price + liters_price

discount_price = total_price * (100 - discount_percent) / 100

print(discount_price)
