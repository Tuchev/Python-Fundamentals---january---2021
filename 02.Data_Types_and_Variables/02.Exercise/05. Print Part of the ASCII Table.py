start_num = int(input())
end_num = int(input())

for symbol in range(start_num, end_num + 1):
    print(f"{chr(symbol)} ", end="")