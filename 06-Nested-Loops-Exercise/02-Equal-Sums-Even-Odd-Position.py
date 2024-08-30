first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number + 1):
    num_as_str = str(num)
    even_sum = 0
    odd_sum = 0
    for idx, digit in enumerate(num_as_str):
        if idx % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(num, end=" ")
