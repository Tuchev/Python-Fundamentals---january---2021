words = input().split()

word1 = words[0]
word2 = words[1]

total_sum = 0

min_length = min(len(word1), len(word2))
max_length = max(len(word1), len(word2))

for index in range(min_length):
    total_sum += ord(word1[index]) * ord(word2[index])

if len(word1) > len(word2):
    for index in range(min_length, max_length):
        total_sum += ord(word1[index])
elif len(word2) > len(word1):
    for index in range(min_length, max_length):
        total_sum += ord(word2[index])
print(total_sum)