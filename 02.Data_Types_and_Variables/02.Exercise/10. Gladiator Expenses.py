lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_price = 0
count_for_shield = 0

for fights in range(1, lost_fights_count + 1):
    if fights % 2 == 0:
        total_price += helmet_price
    if fights % 3 == 0:
        total_price += sword_price
    if fights % 2 ==0 and fights % 3 == 0:
        total_price += shield_price
        count_for_shield += 1
        if count_for_shield % 2 == 0:
            total_price += armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")