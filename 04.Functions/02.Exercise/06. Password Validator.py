def chek_password_valid(pword):
    is_valid = True
    consist_only_of_letters_and_digits = True
    count_digits = 0

    if len(pword) < 6 or len(pword) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    for el in pword:
        if el.isdigit():
            count_digits += 1
    #     if not el.isdigit() and not el.isalpha():
    #         consist_only_of_letters_and_digits = False
    #         is_valid = False
    #
    # if not consist_only_of_letters_and_digits:
    #     print("Password must consist only of letters and digits")
    if not pword.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    if count_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


password = input()
result = chek_password_valid(password)

if result:
    print("Password is valid")