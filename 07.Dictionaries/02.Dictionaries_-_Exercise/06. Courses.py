data = input()

all_courses = {}

while not data == "end":
    data = data.split(" : ")
    course_name = data[0]
    user = data[1]
    if course_name not in all_courses:
        all_courses[course_name] = [user]
    else:
        all_courses[course_name].append(user)

    data = input()
sorted_total = sorted(all_courses.items(), key=lambda kvp: -len(kvp[1]))
for key, value in sorted_total:
    print(f"{key}: {len(value)}")
    value = sorted(value)
    for val in value:
        print(f"-- {val}")