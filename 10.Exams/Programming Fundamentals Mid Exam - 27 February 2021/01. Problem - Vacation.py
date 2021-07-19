trip_days = int(input())
budget = float(input())
number_of_people = int(input())
fuel_price_per_km = float(input())
food_expenses = float(input())
night_pppn = float(input())

total_food_expenses = trip_days * number_of_people * food_expenses
total_cost_hotel = number_of_people * night_pppn * trip_days
if number_of_people > 10:
    total_cost_hotel *= 0.75
current_expenses = total_cost_hotel + total_food_expenses
fuel_expenses = 0

for i in range(1, trip_days + 1):
    distance = int(input())
    fuel_expenses = distance * fuel_price_per_km
    current_expenses += fuel_expenses

    if i % 3 == 0 or i % 5 == 0:
        current_expenses *= 1.4
    if i % 7 == 0:
        current_expenses -= (current_expenses / number_of_people)
    if current_expenses > budget:
        diff = abs(current_expenses - budget)
        print(f'Not enough money to continue the trip. You need {diff:.2f}$ more.')
        break

if budget >= current_expenses:
    diff = abs(budget - current_expenses)
    print(f'You have reached the destination. You have {diff:.2f}$ budget left.')