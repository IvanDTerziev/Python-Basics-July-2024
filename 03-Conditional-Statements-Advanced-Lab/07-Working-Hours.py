hour = int(input())
day = input()

day_off = ["Sunday"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day in working_days and 10 <= hour <= 18:
    print("open")
else:
    print("closed")
