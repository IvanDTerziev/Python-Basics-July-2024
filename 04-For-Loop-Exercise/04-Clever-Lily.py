age = int(input())
price_washing_machine = float(input())
toy_price = int(input())

savings = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        savings += birthday * 10 / 2
        savings -= 1
    else:
        savings += toy_price

if savings >= price_washing_machine:
    print(f"Yes! {savings - price_washing_machine:.2f}")
else:
    print(f"No! {price_washing_machine - savings:.2f}")
