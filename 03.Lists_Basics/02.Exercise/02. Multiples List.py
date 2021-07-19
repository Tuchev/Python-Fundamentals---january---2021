factor = int(input())
count = int(input())

number_list = []
number_list.append(factor)
new_number = factor

for num in range(1, count):
    new_number += factor
    number_list.append(new_number)
print(number_list)