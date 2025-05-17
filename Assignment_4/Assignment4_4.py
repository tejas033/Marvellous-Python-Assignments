# Assignment4_4.py

# Python program to use Filter, Map, Reduce, take "n" numeric elements, 
# Filter out even numbers 
# Map to compute square of number
# Reduce to perform sum of all the numbers

from functools import reduce

CheckEven = lambda no : (no%2 == 0)
Square = lambda no : (no ** 2)
Sum = lambda no1, no2 : (no1 + no2)

def main():
    print("Enter number of elements: ")
    size = int(input())
    Data = list()

    print("Input List: ")
    for i in range (size):
        Data.append(int(input()))

    FData           = list(filter(CheckEven, Data))
    print("List after filter: ", FData)

    MData           = list(map(Square, FData))
    print("Map after filter: ", MData)

    ReduceValue     = reduce(Sum, MData)
    print("Output of Reduce: ", ReduceValue)

if __name__ == "__main__":
    main()