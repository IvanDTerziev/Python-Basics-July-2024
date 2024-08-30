max_num = float('-inf')
sum_numbers = 0

n = int(input())

for i in range(n):
    num = int(input())

    sum_numbers += num

    if num > max_num:
        max_num = num

rest = sum_numbers - max_num

if max_num == rest:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    diff = abs(max_num - rest)
    print(f"Diff = {diff}")

# Тук можем да използваме float('-inf'), който ни гарантира, че всяко число, което потребителят въведе,
# Ще бъде по-голямо от първоначалната стойност на max_num