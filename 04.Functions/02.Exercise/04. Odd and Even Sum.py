def get_odd_even_sum(numbers_as_string):
    odd_sum = 0
    even_sum = 0
    for char in numbers_as_string:
        current_char_as_string = int(char)
        if current_char_as_string % 2 == 0:
            odd_sum += current_char_as_string
        else:
            even_sum += current_char_as_string
    return [odd_sum, even_sum]


num_as_string = input()
result = get_odd_even_sum(num_as_string)
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")