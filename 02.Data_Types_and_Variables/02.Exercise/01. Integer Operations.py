from math import trunc
num_a = int(input())
num_b = int(input())
num_c = int(input())
num_d = int(input())

sum_a_b = num_a + num_b

divide = trunc(sum_a_b / num_c)

result = divide * num_d

print(result)