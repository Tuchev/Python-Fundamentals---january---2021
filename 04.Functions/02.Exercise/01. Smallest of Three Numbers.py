def find_smallest(num_1, num_2, num_3):
    if num_1 < num_2 and num_1 < num_3:
        return num_1
    elif num_2 < num_1 and num_2 < num_3:
        return num_2
    elif num_3 < num_1 and num_3 < num_2:
        return num_3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = find_smallest(num_1, num_2, num_3)
print(result)