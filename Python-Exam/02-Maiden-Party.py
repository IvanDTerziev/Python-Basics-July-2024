LOVE = 0.60
ROSE = 7.20
KEYCHAIN = 3.60
CARICATURE = 18.20
SURPRISE = 22

price_party = float(input())
count_love_sms = int(input())
count_roses = int(input())
count_keychain = int(input())
count_caricature = int(input())
count_surprise = int(input())

discount = 1

if (count_love_sms + count_roses + count_keychain + count_caricature + count_surprise) >= 25:
    discount = 0.65

total = (count_love_sms * LOVE + count_roses * ROSE + count_keychain * KEYCHAIN + count_caricature * CARICATURE
         + count_surprise * SURPRISE) * discount

total *= 0.9

if price_party <= total:
    print(f"Yes! {(total - price_party):.2f} lv left.")
else:
    print(f"Not enough money! {(price_party - total):.2f} lv needed.")
