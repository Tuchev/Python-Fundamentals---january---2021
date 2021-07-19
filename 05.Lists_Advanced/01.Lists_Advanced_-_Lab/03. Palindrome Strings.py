string = input().split()
searched_palindrome = input()
palindrome = []

for word in string:
    if word == "".join(reversed(word)):
        palindrome.append(word)

print(palindrome)
print(f"Found palindrome {palindrome.count(searched_palindrome)} times")