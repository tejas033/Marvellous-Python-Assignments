# Assignment7_3.py

# Take list of numbers, filter only even numbers

CheckEven = lambda no1 : ( no1 % 2 == 0 )

def main():
    lstNumbers = list(map(int, input("Enter list: ").split()))
    print("Even numbers: ", list(filter(CheckEven, lstNumbers)))

if __name__ == "__main__":
    main()