count = 1
total= 0

while count <= 5:
    expense = int(input(f"Enter expense {count}:"))
    total = total + expense
    print("Expense record:₹",expense)
    count = count + 1
print("===Total Expense===",total)
