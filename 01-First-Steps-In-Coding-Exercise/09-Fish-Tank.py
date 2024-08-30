length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

total_volume_in_liters = length * width * height / 1000
liters_needed = total_volume_in_liters * (1 - percent)


print(liters_needed)
