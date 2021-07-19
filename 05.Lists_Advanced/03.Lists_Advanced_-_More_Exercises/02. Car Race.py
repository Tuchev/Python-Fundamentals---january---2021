game_points = [int(x) for x in input().split()]
finish_line = (len(game_points) - 1) // 2

left_racer = game_points[:finish_line]
right_racer = list(reversed(game_points[finish_line + 1:]))
if left_racer.count(0) > 0:
    zero_position = left_racer.index(0)
    before_zero = sum(left_racer[: zero_position]) * 0.8
    after_zero = sum(left_racer[zero_position + 1:])
    score_left_racer = before_zero + after_zero
else:
    score_left_racer = sum(left_racer)

if right_racer.count(0) > 0:
    zero_position = right_racer.index(0)
    before_zero = sum(right_racer[:zero_position]) * 0.8
    after_zero = sum(right_racer[zero_position + 1:])
    score_right_racer = before_zero + after_zero
else:
    score_right_racer = sum(right_racer)

if score_left_racer < score_right_racer:
    print(f"The winner is left with total time: {score_left_racer:.1f}")
else:
    print(f"The winner is right with total time: {score_right_racer:.1f}")