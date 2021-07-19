dungeons_rooms = input().split("|")

health = 100
diff_health = 0
healed = 0
bitcoins = 0
count_of_rooms = 0
is_died = False

for room in dungeons_rooms:
    room = room.split()
    type = room[0]
    size = int(room[-1])
    count_of_rooms += 1
    if type == "potion":
        health += size
        if health > 100:
            diff_health = health - 100
            healed = size - diff_health
            health = 100
            print(f"You healed for {healed} hp.")
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {size} hp.")
            print(f"Current health: {health} hp.")
    elif type == "chest":
        bitcoins += size
        print(f"You found {size} bitcoins.")
    else:
        health -= size
        if health > 0:
            print(f"You slayed {type}.")
        else:
            print(f"You died! Killed by {type}.")
            print(f"Best room: {count_of_rooms}")
            is_died = True
            break
if not is_died:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")