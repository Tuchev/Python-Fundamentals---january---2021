data = input()
products = {}
count = 1
last_product = data


while not data == "stop":
    if count % 2 != 0:
        if data not in products:
            products[data] = 0
        last_product = data
    else:
        products[last_product] += int(data)
    count += 1
    data = input()

for product, value in products.items():
    print(f"{product} -> {value}")