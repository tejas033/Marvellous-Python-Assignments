
# Assignment5_1.py

# take two numbers from user, perform Sum, Difference, Product, Division operations

def Sum(no1, no2):
    return (no1 + no2)

def Difference(no1, no2):
    return (no1 - no2)

def Product(no1, no2):
    return (no1 * no2)

def Division(no1, no2):
    return (no1 / no2)

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    print()

    print("Sum: ",          Sum(no1, no2))
    print("Difference: ",   Difference(no1, no2))
    print("Product: ",      Product(no1, no2))
    print("Division: ",     Division(no1, no2))

if __name__ == "__main__":
    main()
