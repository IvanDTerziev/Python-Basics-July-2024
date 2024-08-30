actor_name = input()
points_from_academy = float(input())
judges_count = int(input())
is_points_enough = False

for judges in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    points_from_academy += ((len(judge_name) * judge_points) / 2)

    if points_from_academy >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!")
        is_points_enough = True
        break

else:
    if not is_points_enough:
        print(f"Sorry, {actor_name} you need {(1250.5 - points_from_academy):.1f} more!")
