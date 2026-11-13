def show_title():
    print("==== EXPENSE ANALYSIS ====")

def calculate_total(expenses):
    return sum(expenses)

def find_highest(expenses):
    if len(expenses) == 0:
        return 0
    return max(expenses)

def find_lowest(expenses):
    if len(expenses) == 0:
        return 0
    return min(expenses)

def calculate_average(expenses):
    if len(expenses) == 0:
        return 0
    return sum(expenses) / len(expenses)



