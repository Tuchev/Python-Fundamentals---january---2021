shot_target = [int(target) for target in input().split()]

counter = 0

command = input()
while not command == "End":
    index = int(command)
    if index < len(shot_target) and shot_target[index] > -1:
        target = shot_target[index]
        shot_target[index] = -1
        for i, num in (enumerate(shot_target)):
            if num == -1:
                continue
            if target < num:
                shot_target[i] -= target
            elif target >= num and num > -1:
                shot_target[i] += target
        counter += 1
    command = input()
print(f"Shot targets: {counter} ->", end=" ")
print(" ".join(map(str, shot_target)))