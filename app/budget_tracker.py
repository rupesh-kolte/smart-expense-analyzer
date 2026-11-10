print ("==== SMART BUDGET TRACKER ====")
budget = int(input("Enter monthly budget:"))
count = 1
total = 0
while count <= 5:
    expense = int(input(f"Enter expense {count}:"))
    total = total + expense
    count = count + 1
print("==== MONTHLY SUMMARY ====")
print("Monthly Budget:₹",budget)
print("Total Expenses:₹",total)
remaining = budget - total
print("Remaining Balance:₹",remaining)
if remaining < 0: 
    print("Budget Exceeded!")
elif remaining == 0:
    print("Budget Fully Used!")
else:
    print("You are within a budget!")