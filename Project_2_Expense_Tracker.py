# Project 2: Expense Tracker
# DecodeLabs Python Programming Internship

total = 0

while True:
    expense = input("Enter expense amount (or 'q' to quit): ")

    if expense.lower() == "q":
        break

    try:
        new_expense = float(expense)
        total = total + new_expense
        print("Expense added successfully!")
        print("Current Total Spent:", total)

    except ValueError:
        print("Invalid input. Please enter a number.")

print("\n===== EXPENSE TRACKER =====")
print(f"Total Spent: ₹{total:.2f}")



