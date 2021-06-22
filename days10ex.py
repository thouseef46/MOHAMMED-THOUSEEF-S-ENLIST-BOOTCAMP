class Bank_Account:
    def _init_(self):
        self.balance=0
        print("deposit and withdrawal")

    def deposite(self):
        amount=float(input("enter the amount to deposite"))
        self.balance += amount
        print("amount deposite:",amount)

    def withdrawl(self):
        amount=float(input("enter the amount to withdrawal"))
        if self.balance >= amount:
            self.balance -=amount
            print("amount withdrawal:",amount)
        else:
            print("insufficient of balance")

    def display(self):
        print("net available balance:",amount)


s = Bank_Account()

s.deposite()
s.withdawal()
s.display()

