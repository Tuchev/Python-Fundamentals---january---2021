number = ["2", "4", "7", "0", "-3", "-22"]
new_number = 0
reverse_number_list = []

for i in range(len(number)):
    # if int(number[i]) > 0:
    new_number = int(number[i]) * -1
    reverse_number_list.append(new_number)
    # elif int(number[i]) < 0:
    #     new_number = int(number[i]) * -1
    #     reverse_number_list.append(new_number)
    # elif int(number[i]) == 0:
    #     reverse_number_list.append(int(number[i]))
print(reverse_number_list)