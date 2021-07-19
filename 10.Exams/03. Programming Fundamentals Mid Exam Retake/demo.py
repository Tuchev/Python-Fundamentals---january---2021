targets_sequence_integers = list(map(int, input().split()))
counter = 0

while True:
    command = input()
    if command == "End":
        break
    else:
        index = int(command)
        if index < len(targets_sequence_integers) and targets_sequence_integers[index] > -1:
            target = targets_sequence_integers[index]
            targets_sequence_integers[index] = -1
            for i, num in (enumerate(targets_sequence_integers)):
                if num == -1:
                    continue
                if target < num:
                    targets_sequence_integers[i] -= target
                elif target >= num and num > -1:
                    targets_sequence_integers[i] += target
            counter += 1

print(f"Shot targets: {counter} ->", end=" ")
print(" ".join(map(str, targets_sequence_integers)))