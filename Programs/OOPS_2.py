class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debit from Account")
        print("Total Balance is ", self.get_balance())
    
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credit to Account")
        print("Total Balance is ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, "123456")
acc1.debit(1000)
acc1.credit(1500)   
acc1.credit(49500)  
acc1.debit(10000)   