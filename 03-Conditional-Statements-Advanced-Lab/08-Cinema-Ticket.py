day_from_week = input()

days_with_12 = ("Monday", "Tuesday", "Friday")
days_with_14 = ["Wednesday", "Thursday"]
days_with_16 = ["Saturday", "Sunday"]

if day_from_week in days_with_12:
    print("12")
elif day_from_week in days_with_14:
    print("14")
elif day_from_week in days_with_16:
    print("16")
