PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT_FOR_KIDS_AND_STUDENTS = 5.00

type_of_project = input()
number_of_rows = int(input())
number_of_columns = int(input())
income = 0

cinema_capacity = number_of_rows * number_of_columns

if type_of_project == "Premiere":
    income = cinema_capacity * PREMIERE
elif type_of_project == "Normal":
    income = cinema_capacity * NORMAL
elif type_of_project == "Discount":
    income = cinema_capacity * DISCOUNT_FOR_KIDS_AND_STUDENTS
print(f"{income:.2f} leva")
