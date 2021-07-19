def calc_factorial(num):
    factorial = 1
    for n in range(2, num + 1):
        factorial *= n
    return factorial


def get_factorial_divisions(n1, n2):
    return calc_factorial(n1) / calc_factorial(n2)


num1 = int(input())
num2 = int(input())
result = get_factorial_divisions(num1, num2)
print(f"{result:.2f}")