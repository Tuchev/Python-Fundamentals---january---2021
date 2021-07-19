number_str = input().split()
n = int(input())
numbers = []
for num in number_str:
    numbers.append(int(num))

for _ in range(n):
    numbers.remove(min(numbers))
print(numbers)