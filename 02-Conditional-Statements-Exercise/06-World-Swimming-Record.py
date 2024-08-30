record_time = float(input())
meters = float(input())
seconds_per_meter = float(input())
time_lost_per_15_meters = 12.5

number_of_losts = meters // 15
lost_time = number_of_losts * time_lost_per_15_meters

total_time = seconds_per_meter * meters + lost_time

if total_time < record_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time - record_time):.2f} seconds slower.")
