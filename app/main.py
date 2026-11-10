print("Smart Expense Analyzer")
print("Developer: Rupesh Kolte")
print("==== EXPENSE ANALYZER ====")
category = input("Enter category: ")
expense = int(input("Enter expense: "))
budget = int(input("Enter budget: "))
remaining = budget - expense
print("==== EXPENSE SUMMARY ====")
print("Category:",category)
print("Expense:",expense)
print("Budget:",budget)
print("Remaining:₹",remaining)
if remaining < 0: 
    print("Budget Exceeded!")
elif remaining == 0:
    print("Budget Fully Used!")
else:
    print("You are within a budget!")



