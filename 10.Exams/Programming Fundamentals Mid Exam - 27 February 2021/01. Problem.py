needed_experience = float(input())
count_of_battles = int(input())

battlecount = 0
collect_experience = 0
is_collect = False

for battle in range(1, count_of_battles + 1):
    experience_earned_per_battle = float(input())
    battlecount += 1
    collect_experience += experience_earned_per_battle
    if battlecount % 3 == 0:
        collect_experience += experience_earned_per_battle * 0.15
    if battlecount % 5 == 0:
        collect_experience -= experience_earned_per_battle * 0.1
    if battlecount % 15 == 0:
        collect_experience += experience_earned_per_battle * 0.05
    if collect_experience >= needed_experience:
        is_collect = True
        break
if is_collect:
    print(f"Player successfully collected his needed experience for {battlecount} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(needed_experience - collect_experience):.2f} more needed.")