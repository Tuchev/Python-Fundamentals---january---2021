import re

text = input()
pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))"
valids = []
while text:
    valid_websites = [el.group() for el in re.finditer(pattern, text)]
    if valid_websites:
        valids.extend(valid_websites)
    text = input()
print(*valids, sep="\n")