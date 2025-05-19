# Assignment7_2.py

# map() to double the value of numbers in the list

Double = lambda no : no * 2

def main():
    lstNumbers = list(map(int, input("Enter list: ").split()))

    print("Double list: ", list(map(Double, lstNumbers)))

if __name__ == "__main__":
    main()