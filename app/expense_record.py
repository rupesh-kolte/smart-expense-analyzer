print("==== EXPENSE RECORD ====")
category = input("Enter category:")
amount = int(input("Enter amount:"))
description = input("Enter description:")

print("==== EXPENSE DETAILS ====")
expense = {
    "category": category,
    "amount": amount,
    "description": description
}
print(expense)
print("Category:",expense["category"])
print("Amount:₹",expense["amount"])
print("Description",expense["description"])