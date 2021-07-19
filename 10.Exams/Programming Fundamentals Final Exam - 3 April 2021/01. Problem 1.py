text = input()

data = input()

while not data == "End":
    data = data.split()
    command = data[0]
    if command == "Translate":
        replace = data[1]
        replace_with = data[2]
        text = text.replace(replace, replace_with)
        print(text)
    elif command == "Includes":
        text_to_find = data[1]
        if text_to_find in text:
            print("True")
        else:
            print("False")
    elif command == "Start":
        text_to_start = data[1]
        if text.startswith(text_to_start):
            print("True")
        else:
            print("False")
    elif command == "Lowercase":
        text = text.lower()
        print(text)
    elif command == "FindIndex":
        char = data[1]
        print(text.rfind(char))
    elif command == "Remove":
        start_index = int(data[1])
        count = int(data[2])
        text_to_remove = text[start_index:count]
        text = text.replace(text_to_remove, "")
        print(text)


    data = input()
