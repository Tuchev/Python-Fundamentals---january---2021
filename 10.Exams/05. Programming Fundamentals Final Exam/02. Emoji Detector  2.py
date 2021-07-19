from re import findall, finditer

text = input()

emoji_pattern = r"(?P<surrounding>[:]{2}|[\*]{2})[A-Z]{1}[a-z]{2,}(?P=surrounding)"
nums_pattern = r"\d{1}"

emojis = [emoji.group() for emoji in finditer(emoji_pattern, text)]
nums = [int(num) for num in findall(nums_pattern, text)]

threshold = 1
for num in nums:
    threshold *= num

print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in emojis:
    sum_chars = 0
    for char in emoji[2:-2]:
        sum_chars += ord(char)
    if sum_chars >= threshold:
        print(emoji)