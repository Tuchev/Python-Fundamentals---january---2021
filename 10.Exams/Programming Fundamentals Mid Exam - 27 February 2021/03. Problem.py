cards = input().split(":")
new_deck = []

command_data = input()

while not command_data == "Ready":
    if command_data == "Shuffle deck":
        new_deck.reverse()
    if len(command_data.split()) == 2:
        command, item = command_data.split()
        if command == "Add":
            card_name = item
            if not card_name in cards:
                print("Card not found.")
            else:
                new_deck.append(card_name)
        elif command == "Remove":
            card_name = item
            if not card_name in new_deck:
                print("Card not found.")
            else:
                new_deck.remove(card_name)
    if len(command_data.split()) == 3:
        command, card_name, item = command_data.split()
        if command == "Insert":
            index = int(item)
            if not card_name in cards or index < 0 or index > (len(cards) - 1):
                print("Error!")
            else:
                new_deck.insert(index, card_name)
        elif command == "Swap":
            card_name_1 = card_name
            card_name_2 = item
            index_card_name_1 = new_deck.index(card_name_1)
            index_card_name_2 = new_deck.index(card_name_2)
            new_deck.remove(card_name_1)
            new_deck.remove(card_name_2)
            new_deck.insert(index_card_name_1, card_name_2)
            new_deck.insert(index_card_name_2, card_name_1)
    command_data = input()
print(" ".join(new_deck))
