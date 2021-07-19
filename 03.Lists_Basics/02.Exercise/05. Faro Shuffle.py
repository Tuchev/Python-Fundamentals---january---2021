deck = input().split()
number_of_shuffles = int(input())

left_half = []
right_half = []

for shuffles in range(1, number_of_shuffles + 1):
    current_deck = []
    half = int(len(deck)/2)
    left_half = deck[0:half]
    right_half = deck[half::]
    for index_of_card in range(len(left_half)):
        current_deck.append(left_half[index_of_card])
        current_deck.append(right_half[index_of_card])
    deck = current_deck
print(deck)