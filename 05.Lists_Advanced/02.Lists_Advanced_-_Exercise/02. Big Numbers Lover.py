numbers_as_string = input().split()

numbers_desc_as_string = sorted(numbers_as_string, reverse=True)
print("".join(numbers_desc_as_string))