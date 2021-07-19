import re
text = input()
pattern = r"(?<=(/|\=))[A-Z][a-zA-Z][a-zA-Z]+(?=\1)"

matches = [destination.group() for destination in re.finditer(pattern, text)]
travel_points = sum([len(d) for d in matches])
print(f"Destinations: {', '.join(matches)}")
print(f"Travel Points: {travel_points}")