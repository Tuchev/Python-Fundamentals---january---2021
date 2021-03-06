taxes_percentage = 0.2
total_price = 0

command = input()

while not (command == "special" or command == "regular"):
    price = float(command)
    if price <= 0:
        print("Invalid price!")
    else:
        total_price += price
    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    taxes = taxes_percentage * total_price
    total_with_taxes = total_price + taxes
    if command == "special":
        total_with_taxes *= 0.9  # 10% discount
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_with_taxes:.2f}$")