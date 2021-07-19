n = int(input())

opening_bracket = 0
closing_bracket = 0

for row in range(n):
    command = input()
    if command == "(":
        opening_bracket += 1
    elif command == ")":
        closing_bracket += 1
        if (opening_bracket - closing_bracket) != 0:
            print(f"UNBALANCED")
            exit(0)

if opening_bracket == closing_bracket:
    print(f"BALANCED")
else:
    print(f"UNBALANCED")