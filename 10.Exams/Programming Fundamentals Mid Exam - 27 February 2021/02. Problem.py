number_in_string = [int(num) for num in input().split()]
new_num = []

command_list = input()

while not command_list == "end":
    command_list.split()
    if "remove" in command_list:
        command, item = command_list.split()
        index = int(item)
        new_num = number_in_string[index::]
        number_in_string.clear()
        number_in_string = new_num
        number_in_string = [str(num) for num in number_in_string]
    elif "reverse" in command_list:
        command_list_2 = command_list.split()
        start_index = int(command_list_2[2])
        count = int(command_list_2[4])
        end_index = start_index + count
        list_1 = number_in_string[:start_index]
        list_2 = (number_in_string[start_index:end_index])
        list_2.reverse()
        list_3 = number_in_string[end_index::]
        number_in_string.clear()
        number_in_string = list_1 + list_2 + list_3
        number_in_string = [str(num) for num in number_in_string]
    elif "sort" in command_list:
        command_list_2 = command_list.split()
        start_index = int(command_list_2[2])
        count = int(command_list_2[4])
        end_index = start_index + count
        list_1 = number_in_string[:start_index]
        list_2 = number_in_string[start_index:end_index]
        list_2.sort()
        list_3 = number_in_string[end_index::]
        number_in_string.clear()
        number_in_string = list_1 + list_2 + list_3
        number_in_string = [str(num) for num in number_in_string]
    command_list = input()
print(command_list)
print(", ".join(number_in_string))