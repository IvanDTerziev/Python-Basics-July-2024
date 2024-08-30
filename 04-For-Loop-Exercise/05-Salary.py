Facebook = 150
Instagram = 100
Reddit = 50

tabs = int(input())
salary = int(input())

for i in range(tabs):
    website = input()

    if website == "Facebook":
        salary -= Facebook
        if salary <= 0:
            break

    elif website == "Instagram":
        salary -= Instagram
        if salary <= 0:
            break

    elif website == "Reddit":
        salary -= Reddit
        if salary <= 0:
            break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
