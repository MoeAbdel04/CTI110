# A Travel Expense calculator
# Date: 9/26/23
# CTI-110 P1HW2 - Travel Expense
# Mahamed Abdel

# Pseudocode:
# 1. Ask the user to enter their budget.
# 2. Ask the user to enter the travel destination.
# 3. Ask the user for the amount they will spend on gas.
# 4. Ask the user for the amount they will spend on accommodation.
# 5. Ask the user for the amount they will spend on food.
# 6. Calculate the total expenses (gas + accommodation + food).
# 7. Calculate the remaining budget (budget - total expenses).
# 8. Display the travel expenses including location, initial budget, individual expenses, and remaining balance.

# Prompt the user to enter their budget
budget = float(input("Enter Budget: "))

# Ask the user to enter the travel destination
destination = input("Enter your travel destination: ")

# Ask the user for the amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas? "))

# Ask the user for the amount they will spend on accommodation
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))

# Ask the user for the amount they will spend on food
food_expense = float(input("Last, how much do you need for food? "))

# Calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate the remaining budget
remaining_budget = budget - total_expenses

# Display the travel expenses in a fancy format
print("\n****************************************")
print("             Travel Expenses             ")
print("****************************************")
print("Location:                ", destination)
print("Initial Budget:          $", format(budget, '.2f'))
print("Fuel:                    $", format(gas_expense, '.2f'))
print("Accommodation:           $", format(accommodation_expense, '.2f'))
print("Food:                    $", format(food_expense, '.2f'))
print("Remaining Balance:       $", format(remaining_budget, '.2f'))
print("****************************************")
