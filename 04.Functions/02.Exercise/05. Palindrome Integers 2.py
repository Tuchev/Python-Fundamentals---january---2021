def chek_if_palindrome(el):
    if el == el[::-1]:
        return True
    return False



nums_as_string = input().split(", ")

for num_as_str in nums_as_string:
    print(chek_if_palindrome(num_as_str))