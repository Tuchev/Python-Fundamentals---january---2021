energy = int(input())
command = input()
count = 0
is_Game_end = True

while not command == "End of battle":
    distance = int(command)
    if (energy - distance) < 0:
        is_Game_end = False
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        break
    energy -= distance
    count += 1
    if count % 3 == 0:
        energy += count
    command = input()

if is_Game_end:
    print(f"Won battles: {count}. Energy left: {energy}")