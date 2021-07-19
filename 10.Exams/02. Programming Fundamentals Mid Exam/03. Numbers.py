numbers = [int(num) for num in input().split()]

new_numbers = []
count = 0

if len(numbers) > 1:
    average_number = sum(numbers) / len(numbers)
    numbers = [num for num in numbers if num > average_number]
    numbers.sort()
    numbers.reverse()
    if len(numbers) > 1:
        for num in numbers:
            count += 1
            new_numbers.append(num)
            if count > 4:
                break
        print(" ".join(map(str, new_numbers)))
    else:
        print("No")
else:
    print("No")