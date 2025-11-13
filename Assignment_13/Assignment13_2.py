# OOPs demo :: BankAccount
# Instance variables :: Name & Amount
# Class variable :: ROI (rate of interest) = 10.5

class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print(f'Name: {self.Name} has Amount: {self.Amount}')

    def Deposit(self, depositAmt):
        self.Amount = self.Amount + depositAmt
        return self.Amount

    def Withdraw(self, withdrawAmt):
        self.Amount = self.Amount - withdrawAmt

    def CalculateInterest(self):
        interestAmt = self.Amount * BankAccount.ROI / 100
        return interestAmt

def main():
    # obj1
    obj1 = BankAccount('Ganesh', 5000)
    obj1.Display()
    obj1.Deposit(2000)
    print(f'After deposit & adding interest...')
    obj1.Deposit(obj1.CalculateInterest())
    obj1.Display()

    obj1.Withdraw(1000)
    print(f'After withdraw of 1000...')
    obj1.Display()

    print('---------------------')

    # obj2
    obj2 = BankAccount('Rama', 5001)
    obj2.Display()
    obj2.Deposit(2001)
    print(f'After deposit & adding interest...')
    obj2.Deposit(obj2.CalculateInterest())
    obj2.Display()

    obj2.Withdraw(1000)
    print(f'After withdraw of 1000...')
    obj2.Display()
    
if __name__ == "__main__":
    main()