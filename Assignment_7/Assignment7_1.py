# Assignment7_1.py
# lambda function to calculate square and cube of a number

Square = lambda no1 : no1 * no1
Cube = lambda no1 : no1 ** 3

def main():
    number = int(input("Enter a number: "))
    print("Square:", Square(number))
    print("Cube:", Cube(number))

if __name__ == "__main__":
    main()
