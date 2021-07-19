text = input()

new_text = ""

for index in range(len(text)):
    new_letter = 3 + ord(text[index])
    new_text += chr(new_letter)
print(new_text)