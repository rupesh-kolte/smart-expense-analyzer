print("==== EXPENSE LIST ====")
expenses = []
count = 1
while count <= 5:
    expense = int(input(f"Enter expense {count}:"))
    count = count + 1
    expenses.append(expense)

print("==== SUMMARY ====")
print("All Expenses:",expenses)
total = sum(expenses)
print("Total Expenses:₹",total)
highest = max(expenses)
print("Highest Expense:₹",highest)
lowest = min(expenses)
print("Lowest Expense:₹",lowest)
no_of_expenses = len(expenses)
print("Number of Expenses:",no_of_expenses)
average = sum(expenses) / len(expenses)
print("Average Expense:₹",average)

