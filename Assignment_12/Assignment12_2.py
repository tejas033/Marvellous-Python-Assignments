# OOPs demo 2 ... Circle class and respective

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, radius):
        self.Radius = radius

    def CalculateArea(self):
        return self.PI * self.Radius ** 2
        
    def CalculateCircumference(self):
        return 2 * self.PI * self.Radius
    
    def Display(self):
        self.Area = self.CalculateArea()
        self.Circumference = self.CalculateCircumference()

        print(f'Radius: {self.Radius} Area: {self.Area} Circumference: {self.Circumference}')

def main():
    rad1 = int(input('Enter radius of first circle: '))
    rad2 = int(input('Enter radius of second circle: '))

    obj1 = Circle()
    obj2 = Circle()

    obj1.Accept(rad1)
    obj1.Display()
    
    obj2.Accept(rad2)
    obj2.Display()

if __name__ == '__main__':
    main()