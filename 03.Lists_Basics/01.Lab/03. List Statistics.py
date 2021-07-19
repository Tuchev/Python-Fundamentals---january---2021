n = int(input())
positives_numbers = []
negatives_numbers = []

for i in range(n):
    number = int(input())
    if number >= 0:
        positives_numbers.append(number)
    else:
        negatives_numbers.append(number)
print(positives_numbers)
print(negatives_numbers)
print(f"Count of positives: {len(positives_numbers)}. Sum of negatives: {sum(negatives_numbers)}")