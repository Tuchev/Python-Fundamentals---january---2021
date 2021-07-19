n = int(input())

count = 0
total_liters = 0
capacity = 255
is_full = False
total_count_full = 0

while count != n:
    liters = int(input())
    total_liters += liters
    if total_liters > capacity:
        total_liters -= liters
        is_full = True
        print(f"Insufficient capacity!")
    count += 1

if is_full:
    print(f"{total_liters}")
else:
    print(f"{total_liters}")