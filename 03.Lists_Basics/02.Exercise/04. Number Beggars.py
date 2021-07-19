numbers_as_string = input().split(", ")
number_of_beggars = int(input())

start_index = 0
sum_of_each_beggar = []

for beggar in range(1, number_of_beggars + 1):
    current_sum = 0
    for sum in range(start_index, len(numbers_as_string), number_of_beggars):
        current_sum += int(numbers_as_string[sum])
    sum_of_each_beggar.append(current_sum)
    start_index += 1
print(sum_of_each_beggar)