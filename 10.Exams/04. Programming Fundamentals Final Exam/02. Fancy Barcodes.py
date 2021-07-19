import re

n = int(input())

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for _ in range(n):
    data = input()
    barcode = [valid.group() for valid in re.finditer(pattern, data)]
    group = ""
    bar = "".join(barcode)
    for x in bar:
        if x.isdigit():
            group = group + x

    if not group.isdigit():
        group = "00"
    if barcode:
        print(f"Product group: {group}")
    else:
        print(f"Invalid barcode")