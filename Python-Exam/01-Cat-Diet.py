GRAM_FAT = 9
GRAM_PROTEIN = 4
GRAM_CARBS = 4

fats = int(input())
proteins = int(input())
carbs = int(input())
calories = int(input())
water = int(input())

total_grams_of_fat = ((fats / 100) * 2500) / GRAM_FAT
total_grams_of_protein = ((proteins / 100) * 2500) / GRAM_PROTEIN
total_grams_of_carbs = ((carbs / 100) * 2500) / GRAM_CARBS

weight = total_grams_of_fat + total_grams_of_protein + total_grams_of_carbs
calories_per_gram = 2500 / weight

calories_without_water = calories_per_gram * (1 - water / 100)
print(f"{calories_without_water:.4f}")
