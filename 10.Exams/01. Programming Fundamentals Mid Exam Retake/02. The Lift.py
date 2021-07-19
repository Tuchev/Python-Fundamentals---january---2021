passengers = int(input())
lift_status = [int(m) for m in input().split()]

for i in range(len(lift_status)):
    if int(lift_status[i]) < 4 and passengers > 0:
        p_for_w = min(4 - int(lift_status[i]), passengers)
        lift_status[i] += p_for_w
        passengers -= p_for_w
    if passengers == 0 and sum(lift_status) / len(lift_status) < 4:
        lift_status = list(map(str, lift_status))
        print(f"The lift has empty spots!")
        print(' '.join(lift_status))
        break
    elif passengers > 0 and sum(lift_status) / len(lift_status) == 4:
        lift_status = list(map(str, lift_status))
        print(f"There isn't enough space! {passengers} people in a queue!")
        print(' '.join(lift_status))
        break
    elif passengers == 0 and sum(lift_status) / len(lift_status) == 4:
        lift_status = list(map(str, lift_status))
        print(' '.join(lift_status))
        break