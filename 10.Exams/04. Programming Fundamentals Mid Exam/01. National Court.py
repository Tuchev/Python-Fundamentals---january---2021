people_per_hour_employee_1 = int(input())
people_per_hour_employee_2 = int(input())
people_per_hour_employee_3 = int(input())
all_people = int(input())

total_people_for_one_hour = people_per_hour_employee_1 + people_per_hour_employee_2 + people_per_hour_employee_3

time_needed = 0

while all_people > 0:
    all_people -= total_people_for_one_hour
    time_needed += 1
    if time_needed % 4 == 0 and time_needed != 0:
        time_needed += 1

print(f"Time needed: {time_needed}h.")