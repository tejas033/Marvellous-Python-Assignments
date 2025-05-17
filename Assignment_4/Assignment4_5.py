# Assignment4_5.py

# Python program to use Filter, Map, Reduce, take "n" numeric elements, 
# Filter out prime numbers 
# Map to double these numbers
# Reduce to fetch maximum number amound the mapped elements

from functools import reduce
import math

def CheckPrimeNumber(no):
    if(no == 1):
        return False
    
    for i in range (2, int(math.sqrt(no)) + 1):
        if(no % i == 0):
            return False
    return True

DoubleNumber = lambda no : (no * 2)

def GetMaxNo(no1, no2):
    if(no1 > no2):
        return no1
    else:
        return no2

def main():
    print("Enter number of elements: ")
    size = int(input())
    Data = list()

    print("Input List: ")
    for i in range (size):
        Data.append(int(input()))

    print("List: ", Data)

    FData = list(filter(CheckPrimeNumber, Data))
    print("List after filter: ", FData)

    MData = list(map(DoubleNumber, FData))
    print("Map after filter: ", MData)

    ReduceValue = reduce(GetMaxNo, MData)
    print("Output of Reduce: ", ReduceValue)

if __name__ == "__main__":
    main()