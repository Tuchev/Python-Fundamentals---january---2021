n = int(input())
count = 0

total_sum = 0

while count != n:
    symbol = input()
    total_sum += ord(symbol)
    count += 1

print(f"The sum equals: {total_sum}")