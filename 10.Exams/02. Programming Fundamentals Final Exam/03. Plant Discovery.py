n = int(input())
plants = {}

for _ in range(n):
    plant_name, rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant_name] = {"rarity": rarity, "ratings": []}

data = input()
while not data == "Exhibition":
    command, command_params = data.split(": ")
    if command == "Rate":
        plant_name, rating = command_params.split(" - ")
        rating = int(rating)
        if plant_name in plants:
            plants[plant_name]["ratings"].append(rating)
        else:
            print("error")
    elif command == "Update":
        plant_name, rarity = command_params.split(" - ")
        rarity = int(rarity)
        if plant_name in plants:
            plants[plant_name]["rarity"] = rarity
        else:
            print("error")
    elif command == "Reset":
        plant_name = command_params
        if plant_name in plants:
            plants[plant_name]["ratings"].clear()
        else:
            print("error")
    else:
        print("error")
    data = input()

for plant_name, value in plants.items():
    if value["ratings"]:
        avg = sum(value["ratings"]) / len(value["ratings"])
    else:
        avg = 0
    plants[plant_name]["avg"] = avg
# sorted_plants = sorted(plants.items(), key = lambda tkvp: (-tkvp[1]["rarity"], -tkvp[1]["avg"]))
sorted_plants = sorted(plants.items(), key = lambda tkvp: (tkvp[1]["rarity"], tkvp[1]["avg"]), reverse=True)

print("Plants for the exhibition:")
for plant_name, values in sorted_plants:
    print(f"- {plant_name}; Rarity: {values['rarity']}; Rating: {values['avg']:.2f}")