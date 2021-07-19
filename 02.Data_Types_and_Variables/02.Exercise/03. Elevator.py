from math import ceil
number_of_people = int(input())
capacity = int(input())

result = ceil(number_of_people / capacity)
print(result)