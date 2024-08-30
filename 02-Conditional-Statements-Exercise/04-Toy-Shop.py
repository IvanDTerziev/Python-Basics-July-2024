puzzle_cost = 2.60
doll_cost = 3.00
teddy_bear_cost = 4.10
minion_cost = 8.20
car_cost = 2.00

vacation_cost = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
cars_count = int(input())

total_count = puzzle_count + doll_count + teddy_bears_count + minions_count + cars_count

total_income = (puzzle_cost * puzzle_count +
                doll_cost * doll_count +
                teddy_bear_cost * teddy_bears_count +
                minion_cost * minions_count +
                car_cost * cars_count)

if total_count >= 50:
    total_income *= 0.75

total_income *= 0.90

if total_income >= vacation_cost:
    print(f"Yes! {total_income - vacation_cost:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_cost - total_income:.2f} lv needed.")
