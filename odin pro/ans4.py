class bank_ac:
    def __init__(self):
        self.balance=0
    def deposite(self):
        amount=float(input("enter amount tobe deposited :"))
        self.balance += amount
        print("amount deposited :",amount)
    def withdraw(self):
        amount = float(input("enter amount to be withdraw :"))
        if self.balance>=amount:
            self.balance-=amount
            print("you withdraw amount of :",amount)
        else:
            print("insufficient balance ")
    def display(self):
        print("Avialable balance =",self.balance)
b=bank_ac()
b.deposite()
b.withdraw()
b.display()
