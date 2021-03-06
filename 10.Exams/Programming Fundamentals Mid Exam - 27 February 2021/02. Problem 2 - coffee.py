coffee_list = input().split()
n = int(input())
count_of_commands = 0
command_data = input()

while not count_of_commands == n:
    command_data = command_data.split()
    count_of_commands += 1

    if "Include" in command_data:
        type_of_coffee = command_data[1]
        coffee_list.append(type_of_coffee)
    elif "Remove" in command_data:
        el_to_remove = command_data[1]
        count_to_remove = int(command_data[2])
        if el_to_remove == "first":
            if len(coffee_list) < count_to_remove:
                continue
            for i in range(count_to_remove):
                coffee_list.pop(0)
        elif el_to_remove == "last":
            if len(coffee_list) < count_to_remove:
                continue
            for i in range(count_to_remove):
                coffee_list.pop(-1)
    elif "Prefer" in command_data:
        index_1 = int(command_data[1])
        index_2 = int(command_data[2])
        if 0 <= index_1 < len(coffee_list) and 0 <= index_2 < len(coffee_list):
            coffee_list[index_1], coffee_list[index_2] = coffee_list[index_2], coffee_list[index_1]
    elif "Reverse" in command_data:
        coffee_list.reverse()
    if count_of_commands == n:
        break
    command_data = input()
print("Coffees:")
print(" ".join(coffee_list))