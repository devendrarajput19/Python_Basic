class BankAccount:
    def __init__(self, account_name, account_no, initial_balance = 0):
        self.account_name = account_name
        self.account_no = account_no
        self.__balance = initial_balance

        self.__transactions = []   # Making Transactions private
        
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.__balance += amount
            self.__transactions.append(f"Deposited = {amount}")
            print(f"{amount} deposited successfully....")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount cannot be less than zero...")
        elif amount > self.__balance:
            print("Insufficient Balance...")
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawn amount = {amount}")
            print("Withdrawl Successfull...")

    def check_balance(self):
        print("Account Balance....")
        print("Name = ", self.account_name)
        print("Account No. = ", self.account_no)
        print("Balance = ", self.__balance)

acc1 = BankAccount("Devendra", "Axis-001", 10000)
acc2 = BankAccount("Mahesh", "Axis-002", 15000)

print("------Devendra's Transactions-------")
acc1.deposit(12000)
acc1.withdraw(5000)
acc1.check_balance()

print("------Mahesh Transactions-------")
acc2.deposit(2000)
acc2.withdraw(7000)
acc2.check_balance()