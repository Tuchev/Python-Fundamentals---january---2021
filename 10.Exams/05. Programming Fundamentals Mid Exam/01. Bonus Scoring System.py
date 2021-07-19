from sys import maxsize

count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())

max_bonus = -maxsize
total_bonus = []
max_lectures = []

if count_of_lectures == 0:
    print(f"Max Bonus: {0}.")
    print(f"The student has attended {0} lectures.")
else:
    for student in range(1, count_of_students + 1):
        attendances_of_student = int(input())
        bonus = round((attendances_of_student / count_of_lectures) * (5 + initial_bonus))
        total_bonus.append(bonus)
        max_lectures.append(attendances_of_student)
    print(f"Max Bonus: {max(total_bonus)}.")
    print(f"The student has attended {max(max_lectures)} lectures.")