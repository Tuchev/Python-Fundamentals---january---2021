key = int(input())
n = int(input())

word = ""

for letter in range(1, n + 1):
    symbol = input()
    word += chr(ord(symbol) + key)
print(word)