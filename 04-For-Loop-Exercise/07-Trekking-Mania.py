number_of_groups = int(input())
counter_Musala = counter_Montblanc = counter_Kilimanjaro = counter_K2 = counter_Everest = 0
counter_people = 0

for group in range(number_of_groups):
    people_in_group = int(input())
    counter_people += people_in_group

    if people_in_group <= 5:
        counter_Musala += people_in_group
    elif 6 <= people_in_group <= 12:
        counter_Montblanc += people_in_group
    elif 13 <= people_in_group <= 25:
        counter_Kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        counter_K2 += people_in_group
    elif people_in_group > 40:
        counter_Everest += people_in_group

print(f"{(counter_Musala / counter_people * 100):.2f}%")
print(f"{(counter_Montblanc / counter_people * 100):.2f}%")
print(f"{(counter_Kilimanjaro / counter_people * 100):.2f}%")
print(f"{(counter_K2 / counter_people * 100):.2f}%")
print(f"{(counter_Everest / counter_people * 100):.2f}%")
