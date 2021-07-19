words = input().split()
command = input()

while not command == "Stop":
    data = command.split()

    if data[0] == "Delete":
        index = int(data[1]) + 1
        if 0 <= index < len(words):
            words.pop(index)
    elif data[0] == "Swap":
        word_1 = data[1]
        word_2 = data[2]
        if word_1 in words and word_2 in words:
            index_1 = words.index(word_1)
            index_2 = words.index(word_2)
            words[index_1], words[index_2] = words[index_2], words[index_1]
    elif data[0] == "Put":
        word = data[1]
        index = int(data[2]) - 1
        if 0 < index <= len(words):
            if index == len(words):
                words.append(word)
            else:
                words.insert(index, word)
    elif data[0] == "Sort":
        words = list(sorted(words, reverse=True))
    elif data[0] == "Replace":
        new_word = data[1]
        old_word = data[2]
        if old_word in words:
            index = words.index(old_word)
            words[index] = new_word

    command = input()

print(*words, sep=" ")