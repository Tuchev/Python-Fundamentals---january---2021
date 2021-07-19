type_of_events = input().split("|")

MAX_ENERGY = 100
energy = 100
ORDER_ENERGY = 30
coins = 100

is_over = True

for event in type_of_events:
    current_event = event.split("-")
    event_type = current_event[0]
    value = int(current_event[-1])
    if event_type == "rest":
        gained_energy = 0

        if energy + value > MAX_ENERGY:
            gained_energy = 0
        else:
            energy += value
            gained_energy = value
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_type == "order":
        if energy >= ORDER_ENERGY:
            energy -= ORDER_ENERGY
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if coins > value:
            coins -= value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            is_over = False
            break

if is_over:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")