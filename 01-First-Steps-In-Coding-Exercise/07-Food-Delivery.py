CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEG_MENU = 8.15
DELIVERY_COST = 2.50

nums_of_chicken_menus = int(input())
nums_of_fish_menus = int(input())
nums_of_veg_menus = int(input())

price_for_chicken_menus = nums_of_chicken_menus * CHICKEN_MENU
price_for_fish_menus = nums_of_fish_menus * FISH_MENU
price_for_veg_menus = nums_of_veg_menus * VEG_MENU

total_menu_price = price_for_chicken_menus + price_for_fish_menus + price_for_veg_menus
dessert_price = total_menu_price * 0.20

total_order_price = total_menu_price + dessert_price + DELIVERY_COST
total_order_price = round(total_order_price, 2)
print(total_order_price)
