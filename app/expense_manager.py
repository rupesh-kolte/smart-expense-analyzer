
def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            if not (amount < float("inf")):
                print("Enter a finite number.")
                continue

            return amount

        except ValueError:
            print("Invalid input! Enter a number.")

def add_expense(expenses):
    print("\n--- ADD EXPENSE ---")

    category = input("Enter category: ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    amount = get_valid_amount("Enter amount: ₹")

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    print("\n--- ALL EXPENSES ---")

    if not expenses:
        print("No expenses recorded.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} "
            f"- ₹{expense['amount']:.2f}"
        )

def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)

def show_summary(expenses):
    print("\n--- EXPENSE SUMMARY ---")

    total = calculate_total(expenses)

    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Number of Expenses: {len(expenses)}")

def check_budget(expenses, budget):
    print("\n--- BUDGET STATUS ---")

    total = calculate_total(expenses)
    remaining = budget - total

    print(f"Monthly Budget: ₹{budget:.2f}")
    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Remaining Balance: ₹{remaining:.2f}")

    if remaining < 0:
        print("Budget Exceeded!")
    elif remaining == 0:
        print("Budget Fully Used!")
    else:
        print("You are within your budget!")

def update_expense(expenses):
    print("\n--- UPDATE EXPENSE ---")

    if not expenses:
        print("No expenses available to update.")
        return

    view_expenses(expenses)

    while True:
        try:
            index = int(input("Enter expense number to update: "))

            if index < 1 or index > len(expenses):
                print("Invalid expense number.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    expense = expenses[index - 1]

    print(f"Current Category: {expense['category']}")
    print(f"Current Amount: ₹{expense['amount']:.2f}")

    new_category = input("Enter new category: ").strip()

    while not new_category:
        print("Category cannot be empty.")
        new_category = input("Enter new category: ").strip()

    new_amount = get_valid_amount("Enter new amount: ₹")

    expense["category"] = new_category
    expense["amount"] = new_amount

    print("Expense updated successfully!")

def delete_expense(expenses):
    print("\n--- DELETE EXPENSE ---")

    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses(expenses)

    while True:
        try:
            index = int(input("Enter expense number to delete: "))

            if index < 1 or index > len(expenses):
                print("Invalid expense number.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    removed_expense = expenses.pop(index - 1)

    print(
        f"Deleted: {removed_expense['category']} "
        f"- ₹{removed_expense['amount']:.2f}"
    )

def show_menu():
    print("\n=================================")
    print("     SMART EXPENSE ANALYZER")
    print("=================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expense Summary")
    print("4. Check Budget Status")
    print("5. Update Expense")
    print("6. Delete Expense")
    print("7. Exit")

def main():
    expenses = []

    print("Welcome to Smart Expense Analyzer!")
    budget = get_valid_amount("Enter monthly budget: ₹")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_summary(expenses)

        elif choice == "4":
            check_budget(expenses, budget)

        elif choice == "5":
            update_expense(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            print("Thank you for using Smart Expense Analyzer!")
            break

        else:
            print("Invalid choice! Select 1 to 7.")

if __name__ == "__main__":
    main()
   