def show_welcome():
  print("Welcome to Smart Expense Analyzer")

def display_budget(budget):
    print("Monthly Budget:₹",budget)

def calculate_remaining(budget,expense):
    return budget - expense
    
def check_budget_status(remaining):
    if remaining < 0: 
      print("Budget Exceeded!")
    elif remaining == 0:
     print("Budget Fully Used!")
    else:
     print("You are within a budget!")


budget = int(input("Enter monthly budget:"))
expense = int(input("Enter expense:"))

show_welcome()
display_budget(budget)
remaining = calculate_remaining(budget,expense)
print("Remaining Balance:",remaining)
check_budget_status(remaining)
