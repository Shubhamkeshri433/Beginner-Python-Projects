class BankAccount:
    def __init__(self, account_holder, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} Deposit successfully")
            self.check_balance()
        else:
            print("Invalid amount")

    def withdraw(self):
        amount = float(input("Enter withdraw amount: "))
        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdraw successfully")
        else:
            print("Insuffient balance")
        

    def show_account(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

    def transfer_money(self, other_account):
        amount = float(input(f"Enter amount to transfer: "))
        if amount <= 0:
            print("Enter a valid amount")
        elif amount > self.balance:
            print("Insuffient Balance")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"{amount} Transfer successfully")


ac_1 = BankAccount("shubham", 0)
ac_2 = BankAccount("ravi", 0)

account = {
    "shubham" : ac_1,
    "ravi" : ac_2
}

while True:
    print("-----Bank of Python-----")
    print("Select an Option")
    print("1: Deposite")
    print("2: Withdraw")
    print("3: Check Balance")
    print("4: Transfer")
    print("5: Exit Bank")

    try:
        Select = int(input("What to do: "))

    except:
        print("Enter a valid option:")
        continue

    if Select == 1:
        try:
            user_name = input("Enter your user_name: ").lower()
            user_account = account[user_name]
            user_account.deposit()

        except:
            print("Enter a valid user_name")
            continue

    elif Select == 2:
        try:
            user_name = input("Enter your user_name: ").lower()
            user_account = account[user_name]
            user_account.withdraw()

        except:
            print("Enter a valid user_name")
            continue

    elif Select == 3:
        try:
            user_name = input("Enter your user_name: ").lower()
            user_account = account[user_name]
            user_account.check_balance()

        except:
            print("Enter a valid user_name")
            continue

    elif Select == 4:
        try:
            user_name = input("Enter your user_name: ").lower()
            user_account = account[user_name]

            transfer_to = input("Enter other account user_name: ").lower()
            transfer_user = account[transfer_to]

            user_account.transfer_money(transfer_user)

        except:
            print("Enter a valid user_names")
            continue

    elif Select == 5:
        print("Goodbye")
        break

    else:
        print("Invalid selection")

