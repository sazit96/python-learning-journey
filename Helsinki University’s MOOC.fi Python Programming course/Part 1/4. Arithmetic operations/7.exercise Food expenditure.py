time_cafeteria = int(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of the typical student lunch?"))
Spend_groceries = float(input("How much money do you spend on groceries in a week?"))
total_week_cost = (time_cafeteria * lunch_price) + Spend_groceries;
print("Average food expenditure:")
print(f"Daily: {total_week_cost / 7} euros")
print(f"Weekly: {total_week_cost} euros")
