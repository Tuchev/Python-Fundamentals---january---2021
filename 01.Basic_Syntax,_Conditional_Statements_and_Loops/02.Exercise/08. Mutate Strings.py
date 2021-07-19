text_1 = input()
text_2 = input()

result = ""
previous_text = text_1

for index in range(len(text_1)):
    for i in range(index +1):
        result += text_2[i]
    for i in range(index +1, len(text_2)):
        result += text_1[i]
    if not result == previous_text:
        print(result)
    previous_text = result
    result = ""