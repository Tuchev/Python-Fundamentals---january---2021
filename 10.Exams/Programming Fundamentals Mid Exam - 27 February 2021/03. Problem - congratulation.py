words = input().split(" ")
command = input()
while command != "Stop":
    action = command.split(" ")
    if action[0] == "Delete":
        if int(action[1]) + 1 < len(words):
            words.pop(int(action[1]) + 1)
    elif action[0] == "Swap":
        if action[1] and action[2] in words:
            i_1 = words.index(action[1])
            i_2 = words.index(action[2])
            words[i_1] = action[2]
            words[i_2] = action[1]
    elif action[0] == "Put":
        if 0 < int(action[2]) < len(words):
            words.insert(int(action[2]) - 1, action[1])
        elif int(action[2]) == 0:
            words.insert(0, action[1])
    elif action[0] == "Sort":
        words.sort(reverse=True)
    elif action[0] == "Replace":
        if action[2] in words:
            a = words.index(action[2])
            words[a] = action[1]
    command = input()
print(" ".join(words))