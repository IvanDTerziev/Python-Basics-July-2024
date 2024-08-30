num = int(input())

left = 0
right = 0
for _ in range(num):
    current_num = int(input())
    left = left + current_num

for _ in range(num):
    current_num = int(input())
    right += current_num

if left == right:
    print(f"Yes, sum = {left}")
else:
    diff = abs(right - left)
    print(f"No, diff = {diff}")
