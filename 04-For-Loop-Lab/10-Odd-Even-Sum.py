n = int(input())

odd = 0
even = 0

for i in range(1, n + 1):
    current = int(input())
    if i % 2 == 0:
        even += current
    else:
        odd += current

if even == odd:
    print(f"Yes\nSum = {even}")
else:
    diff = abs(even - odd)
    print(f"No\nDiff = {diff}")
