import re
text = input()

pattern = r"\+359( |-)[2]\1[0-9]{3}\1[0-9]{4}\b"

valid_numbers = [obj.group() for obj in re.finditer(pattern, text)]
print(", ".join(valid_numbers))