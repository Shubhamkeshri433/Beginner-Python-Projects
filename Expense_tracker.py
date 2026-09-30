expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description
    }

    expenses.append(expense)
    print("Expense added successfully")

def view_expense():
    if not expenses:
        print("Nothing to show")
        return

    for expense in expenses:
        print(
            f"Rs {expense['amount']} | "
            f" Category = {expense['category']} | "
            f" Description = {expense['description']} | "

        )


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense['amount']

    print(f"Total amount: {total}")


while True:
    print("/n ===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choise = input("Enter your choice: ")

    if choise == "1":
        add_expense()

    elif choise == "2":
        view_expense()

    elif choise == "3":
        total_expenses()

    elif choise == "4":
        print("Okay, Goodbye")
        break

    else:
        print("Invalid Choice")