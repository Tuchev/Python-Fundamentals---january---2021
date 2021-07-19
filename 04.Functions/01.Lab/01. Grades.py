def convert_grade_to_string(grade_in_num):
    if 2 <= grade_in_num <= 2.99:
        return "Fail"
    elif 3 <= grade_in_num <= 3.49:
        return "Poor"
    elif 3.50 <= grade_in_num <= 4.49:
        return "Good"
    elif 4.50 <= grade_in_num <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_in_num <= 6.00:
        return "Excellent"


grade = float(input())
print(convert_grade_to_string(grade))