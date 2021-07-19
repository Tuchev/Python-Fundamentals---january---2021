budget = float(input())
price_of_flour = float(input())

number_of_eggs = 0
number_of_cozonac = 0

price_for_1_pack_of_eggs = 0.75 * price_of_flour
price_for_1l_milk = 1.25 * price_of_flour
price_for_milk_for_one_cozonac = price_for_1l_milk / 4

total_price_for_one_cozonac = price_for_1_pack_of_eggs + price_of_flour + price_for_milk_for_one_cozonac

while budget > total_price_for_one_cozonac:
    budget -= total_price_for_one_cozonac
    number_of_cozonac += 1
    number_of_eggs += 3
    if number_of_cozonac % 3 == 0:
        number_of_eggs -= (number_of_cozonac - 2)

print(f"You made {number_of_cozonac} cozonacs! Now you have {number_of_eggs} eggs and {budget:.2f}BGN left.")