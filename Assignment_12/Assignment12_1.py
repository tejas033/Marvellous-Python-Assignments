# OOPs demo 1 ... simple class demo, instance variables, instance methods, and a class variable

class Demo:
    Value = 0               # class variable

    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b

    def Fun(self):          # instance method
        print(f'Inside Fun method... value of no1: {self.no1} value of no2: {self.no2}')

    def Gun(self):          # instance method
        print(f'Inside Gun method... value of no1: {self.no1} value of no2: {self.no2}')

def main():
    # create instance of class Demo
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__ == '__main__':
    main()