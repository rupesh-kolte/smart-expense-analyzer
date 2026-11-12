print("==== MULTIPLE EXPENSE RECORD ====")

expenses = []
count = 1
while count <= 3:
    category = input(f"Enter category {count}:")
    amount = int(input(f"Enter amount {count}:"))
    description = input(f"Enter description {count}:")
    count = count + 1
    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
print("==== ALL EXPENSE RECORDS ====")
total = 0
for expense in expenses:
    print("Category:",expense["category"])
    print("Amount:₹",expense["amount"])
   
    total = total + expense['amount']
print("==== EXPENSE ANALYSIS ====")
print("Total Expenses:",total)
print("Number of Expenses:",len(expenses))
