import re

text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

valid_mactches = [match_obj.group() for match_obj in re.finditer(pattern, text)]
print(*valid_mactches, sep=",")