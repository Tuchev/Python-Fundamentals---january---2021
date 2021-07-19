peoples = int(input())
lift_wagons = [int(wagon) for wagon in input().split()]

is_Full = False
is_no_more_peoples = False

for wagon in range(len(lift_wagons)):
    if lift_wagons[wagon] <= 4 and peoples > 0:
        while not lift_wagons[wagon] == 4:
            peoples -= 1
            lift_wagons[wagon] += 1
            if peoples == 0:
                is_no_more_peoples = True
                break
if is_Full and peoples == 0:
    print("The lift has empty spots!")
    print(" ".join([str(wagon) for wagon in lift_wagons]))
elif not is_Full and peoples > 0:
    print(f"There isn't enough space! {peoples} people in a queue!")
    print(" ".join([str(wagon) for wagon in lift_wagons]))
elif is_Full and peoples == 0:
    print(" ".join([str(wagon) for wagon in lift_wagons]))
