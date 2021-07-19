data = input()

products_prices = {}
products_quantities = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products_prices:
        products_prices[name] = price
        products_prices[quantity] = quantity
    else:
        products_prices[name] = price
        products_prices[quantity] += quantity

    data = input()

for product, price in products_prices.items():
    result = price * products_quantities[product]
    print(f"{product} -> {result:.2f}")