
def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter expense amount: ₹"))

            if amount < 0:
                print("Expense cannot be negative. Try again.")
                continue

            return amount

        except ValueError:
            print("Invalid input! Please enter a valid number.")

def collect_expenses():
    expenses = []

    while True:
        try:
            count = int(input("How many expenses? "))

            if count < 0:
                print("Number of expenses cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

    for i in range(1, count + 1):
        print(f"\nExpense {i}")
        amount = get_valid_amount()
        expenses.append(amount)

    return expenses

def calculate_total(expenses):
    return sum(expenses)

def show_summary(expenses):
    print("\n==== EXPENSE SUMMARY ====")
    print("Expenses:", expenses)
    print("Total Expenses: ₹", calculate_total(expenses))
    print("Number of Expenses:", len(expenses))

def main():
    print("Welcome to Smart Expense Analyzer!")

    expenses = collect_expenses()
    show_summary(expenses)

if __name__ == "__main__":
    main()



            