# Assignment7_4.py

# Take list of numbers, Reduce the list of numbers by multiplying them into single value

from functools import reduce

Product = lambda no1, no2 : ( no1 * no2 )

def main():
    lstNumbers = list(map(int, input("Enter list: ").split()))
    print("Product:", reduce(Product, lstNumbers))

if __name__ == "__main__":
    main()