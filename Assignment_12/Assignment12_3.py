# OOPs demo 3 ... Arithmetic

class Arithmetic:
    def __init__(self):
        self.no1 = 0
        self.no2 = 0

    def Accept(self, val1, val2):
        self.no1 = val1
        self.no2 = val2

    def Addition(self):
        return self.no1 + self.no2
    
    def Subtraction(self):
        return self.no1 - self.no2
    
    def Multiplication(self):
        return self.no1 * self.no2
    
    def Division(self):
        return self.no1 / self.no2

def main():
    
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))

    obj1 = Arithmetic()
    obj1.Accept(no1, no2)

    print("Addition of both numbers is: ", obj1.Addition())
    print("Subtraction of both numbers is: ", obj1.Subtraction())
    print("Multiplication of both numbers is: ", obj1.Multiplication())
    print("Division of both numbers is: ", obj1.Division())

    print()

    # Hard code values to the instance variables
    obj2 = Arithmetic()
    obj2.Accept(50, 10)
    
    print("Addition of 50 & 10 numbers is: ", obj2.Addition())
    print("Subtraction of 50 & 10 numbers is: ", obj2.Subtraction())
    print("Multiplication of 50 & 10 numbers is: ", obj2.Multiplication())
    print("Division of 50 & 10 numbers is: ", obj2.Division())

if __name__ == '__main__':
    main()