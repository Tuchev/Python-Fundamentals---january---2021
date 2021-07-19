text = input()

data = input()
new_text = ""

while not data == "Decode":
    command = data.split("|")
    if command[0] == "ChangeAll":
        replace = command[1]
        replace_with = command[2]
        text = text.replace(replace, replace_with)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        first_part = text[:index]
        second_part = text[index:]
        text = first_part + value + second_part
    elif command[0] == "Move":
        n = int(command[1])
        chars_to_move = text[:n]
        rest_chars = text[n:]
        text = rest_chars + chars_to_move

    data = input()
print(f"The decrypted message is: {text}")