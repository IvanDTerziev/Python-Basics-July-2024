import math

W = 2000
F = 1200
SF = 720

tournaments_counter = int(input())
starting_points_in_ranklist = int(input())

gained_points = 0
win_counter = 0
points = starting_points_in_ranklist

for _ in range(tournaments_counter):
    tournament_position = input()

    if tournament_position == "W":
        points += W
        win_counter += 1
        gained_points += W

    elif tournament_position == "F":
        points += F
        gained_points += F

    elif tournament_position == "SF":
        points += SF
        gained_points += SF

average_points = math.floor(gained_points / tournaments_counter)
win_percentage = win_counter / tournaments_counter * 100

print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")
