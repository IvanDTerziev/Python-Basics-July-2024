failing_students = 0
average_students = 0
good_students = 0
excellent_students = 0
average_grade = 0

students = int(input())

for i in range(1, students + 1):
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        failing_students += 1
        average_grade += grade
    elif 3.00 <= grade <= 3.99:
        average_students += 1
        average_grade += grade
    elif 4.00 <= grade <= 4.99:
        good_students += 1
        average_grade += grade
    elif grade >= 5.00:
        excellent_students += 1
        average_grade += grade

percent_excellent = (excellent_students / students) * 100
percent_good = (good_students / students) * 100
percent_average = (average_students / students) * 100
percent_failing = (failing_students / students) * 100
average_grade /= students

print(f"Top students: {percent_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_average:.2f}%")
print(f"Fail: {percent_failing:.2f}%")
print(f"Average: {average_grade:.2f}")
