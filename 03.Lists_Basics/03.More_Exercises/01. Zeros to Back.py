single_string = input().split(", ")

new_string = []

for el in single_string:
    if int(el) != 0:
        new_string.append(int(el))

number_of_zero = len(single_string) - len(new_string)
for _ in range(number_of_zero):
    new_string.append(0)
print(new_string)