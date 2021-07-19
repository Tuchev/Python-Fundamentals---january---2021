encrypted = input()
encrypted_list = []
if " " in encrypted:
    for char in range(len(encrypted)):
        encrypted_list.append(encrypted[char])
else:
    encrypted.replace("", " ").split()
    for char in range(len(encrypted)):
        encrypted_list.append(encrypted[char])

numbers = []
decrypted = []
non_numbers = []
count = 0
index = 0

for x in range(len(encrypted_list)):
    if encrypted_list[x].isnumeric():
        numbers.append(int(encrypted_list[x]))
    else:
        non_numbers.append(encrypted_list[x])
take_list = [numbers[index] for index in range(len(numbers)) if index % 2 == 0]
skip_list = [numbers[index] for index in range(len(numbers)) if index % 2 == 1]

for i in range(len(take_list)):
    current_take_part = int(take_list[i])
    current_skip_part = int(skip_list[i])
    for add in range(current_take_part):
        decrypted.append(non_numbers[index])
        if len(non_numbers) - 1 < index + 1:
            break
        else:
            index += 1
    count += (current_take_part + current_skip_part)
    index = count
print("".join(decrypted))