numbers_as_string = input().split(", ")

event_number_index =[]

for index in range(len(numbers_as_string)):
    if int(numbers_as_string[index]) % 2 == 0:
        event_number_index.append(index)
print(event_number_index)