string_1 = input().split(", ")
string_2 = input().split(", ")

new_string = []

for word_1 in string_1:
    for word_2 in string_2:
        if word_1 in word_2:
            new_string.append(word_1)
print(sorted(set(new_string), key=new_string.index))