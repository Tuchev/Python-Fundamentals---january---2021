names = input().split(", ")

for name in names:
    if 3 < len(name) < 16:
        if name.isalpha() or name.isdigit() or name.isalnum() or "-" in name or "_" in name:
            print(name)