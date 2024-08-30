pages = int(input())
pages_per_hour = int(input())
total_days = int(input())

hours_needed = pages // pages_per_hour

hours_per_day = hours_needed / total_days

print(int(hours_per_day))
