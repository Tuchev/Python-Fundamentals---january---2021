def solve_palindrome(current_number):
    for i in palindrome_number:
        first_number = i[0]
        end_number = i[-1]
        if first_number == end_number:
            print('True')
        else:
            print('False')


palindrome_number = input().split(', ')
solve_palindrome(palindrome_number)