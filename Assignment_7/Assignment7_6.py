# Assignment7_6.py
# fetch prime numbers from the list of numbers using filter()

import math

def PrimeNumbers(no1):
    for i in range (2, int(math.sqrt(no1)) + 1):
        if(no1 % i == 0 and no1 != 2):
            return False
    return True

def main():
    lstNumbers = list(map(int, input("Enter list: ").split()))
    print("Prime numbers:", list(filter(PrimeNumbers, lstNumbers)))

if __name__ == "__main__":
    main()