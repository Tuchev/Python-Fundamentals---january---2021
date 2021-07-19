def add_and_subtract():
    all_numbers = []
    for number in range(3):
        single_number = input()
        all_numbers.append(single_number)
    first_number = int(all_numbers[0])
    second_number = int(all_numbers[1])
    third_number = int(all_numbers[2])

    def sum_numbers():
        return first_number + second_number

    def subtract():
        return sum_numbers() - third_number

    return subtract()


print(add_and_subtract())