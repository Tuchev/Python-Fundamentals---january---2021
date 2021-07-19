words = input().split()
all_words = {}

for word in words:
    for el in range(len(word)):
        letter = word[el]
        if letter not in all_words:
            all_words[letter] = 0
        all_words[letter] += 1

for letter, quantity in all_words.items():
    print(f"{letter} -> {quantity}")