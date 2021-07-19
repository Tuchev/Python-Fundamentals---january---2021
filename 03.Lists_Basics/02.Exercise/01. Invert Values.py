num_input = input().split()
num_reverse = 0
reverse_num_list = []

# for i in range(len(num_input)):
    # if int(num_input[i]) > 0:
    #     num_reverse = int(num_input[i]) * -1
    #     reverse_num_list.append(num_reverse)
    # elif int(num_input[i]) < 0:
    #     num_reverse = int(num_input[i]) * -1
    #     reverse_num_list.append(num_reverse)
    # elif int(num_input[i]) == 0:
    #     reverse_num_list.append(int(num_input[i]))
# print(reverse_num_list)

for i in range(len(num_input)):
    num_reverse = int(num_input[i]) * -1
    reverse_num_list.append(num_reverse)
print(reverse_num_list)