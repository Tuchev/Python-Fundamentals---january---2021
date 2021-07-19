text = input()
data = input()

while not data == "Done":
    command = data.split()
    if command[0] == "TakeOdd":
        text = text[1::2]
        print(text)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        text = text[:index] + text[index + length:]
        print(text)
    elif command[0] == "Substitute":
        one = command[1]
        two = command[2]
        if one in text:
            text = text.replace(one, two)
            print(text)
        else:
            print('Nothing to replace!')

    data = input()
print(f"Your password is: {text}")