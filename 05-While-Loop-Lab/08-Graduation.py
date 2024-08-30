name = input()

grades = 1
sum_grades = 0.0
excluded = 0

while grades <= 12:
    grade = float(input())

    if grade < 4.00:
        excluded += 1
        if excluded > 1:
            print(f"{name} has been excluded at {grades} grade")
            break
        continue

    sum_grades += grade
    grades += 1

if grades > 12:
    average = sum_grades / 12
    print(f"{name} graduated. Average grade: {average:.2f}")
