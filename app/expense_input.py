from expense_calculator import calculate_total
def collect_expenses():
    count = int(input("How many expenses?"))
    expenses = []
    for i in range(1, count + 1):
        amount = int(input(f"Enter Expense {i}:"))
        expenses.append(int(amount)if amount.is_integer() else amount)
    return expenses

expenses = collect_expenses()
total = calculate_total(expenses)
print("Expenses:",expenses)
print("Total Expenses:₹",total)

    
