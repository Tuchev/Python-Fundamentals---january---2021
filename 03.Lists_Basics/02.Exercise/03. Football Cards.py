cards = input().split()

all_cards = []

team_a = 11
team_b = 11
is_game = False

for card in cards:
    if card in all_cards:
        continue
    all_cards.append(card)
    if team_a < 7 or team_b < 7:
        is_game = True
        break
    if "A" in card:
        team_a -= 1
    elif "B" in card:
        team_b -= 1
print(f"Team A - {team_a}; Team B - {team_b}")
if is_game:
    print(f"Game was terminated")