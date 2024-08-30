upper_limit_of_the_first_number = int(input())
upper_limit_of_the_second_number = int(input())
upper_limit_of_the_third_number = int(input())

for i in range(1, upper_limit_of_the_first_number + 1):
    if i % 2 == 0:
        for j in range(1, upper_limit_of_the_second_number + 1):
            if str(j) in '2357':
                for h in range(1, upper_limit_of_the_third_number + 1):
                    if h % 2 == 0:
                        print(i, j, h)
