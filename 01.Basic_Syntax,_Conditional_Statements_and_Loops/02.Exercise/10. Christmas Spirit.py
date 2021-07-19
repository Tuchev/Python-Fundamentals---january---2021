quantity = int(input())
days = int(input())

christmas_spirit = 0

ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

total_cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ORNAMENT_SET * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        total_cost += (TREE_SKIRT * quantity + TREE_GARLANDS * quantity)
        christmas_spirit += 13
    if day % 5 == 0:
        total_cost += TREE_LIGHTS * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        total_cost += TREE_SKIRT + TREE_GARLANDS + TREE_LIGHTS
        christmas_spirit -= 20
    if day == days and day % 10 == 0:
        christmas_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")