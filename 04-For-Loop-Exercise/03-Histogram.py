counter = int(input())

p1 = p2 = p3 = p4 = p5 = 0

for _ in range(counter):
    current_num = int(input())

    if current_num < 200:
        p1 += 1
    elif current_num < 400:
        p2 += 1
    elif current_num < 600:
        p3 += 1
    elif current_num < 800:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

p1_percent = p1 / counter * 100
p2_percent = p2 / counter * 100
p3_percent = p3 / counter * 100
p4_percent = p4 / counter * 100
p5_percent = p5 / counter * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")
