text = input()

new_text = ""

for i in range(len(text) -1, -1, -1):
    new_text += text[i]
    if ord(text[i-1]) == 92:
        break

words = new_text[::-1]
list_of_words = words.split(".")
print(f"File name: {list_of_words[0]}")
print(f"File extension: {list_of_words[1]}")