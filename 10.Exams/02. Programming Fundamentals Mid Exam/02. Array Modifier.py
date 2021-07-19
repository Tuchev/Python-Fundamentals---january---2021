numbers = [int(num) for num in input().split()]
command_data = input()
multiply_element = 0


while not command_data == "end":
    command_data = command_data.split()
    if len(command_data) > 1:
        command = command_data[0]
        num1 = int(command_data[1])
        num2 = int(command_data[2])
        if command == "swap":
            numbers[num1], numbers[num2] = numbers[num2], numbers[num1]
        elif command == "multiply":
            multiply_element = numbers[num1] * numbers[num2]
            numbers[num1] = multiply_element
    else:
        command = command_data[0]
        numbers = [num - 1 for num in numbers]
    command_data = input()
print(", ".join(map(str, numbers)))