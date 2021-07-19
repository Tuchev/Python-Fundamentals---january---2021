def calculates_a_result(num1, num2, operator):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


operator = input()
num1 = int(input())
num2 = int(input())
print(calculates_a_result(num1, num2, operator))