# Assignment8_3.py

# Multi-threading program to perform sum of even and odd elements from the numeric list

import threading
from functools import reduce

CheckEven = lambda no : (no % 2 == 0)       # filter
CheckOdd = lambda no : (no % 2 != 0)

Sum = lambda no1, no2 : (no1 + no2)         # reduce

def SumOfEven(lst):
    lstEven = list(filter(CheckEven, lst))
    sumEven = reduce(Sum, lstEven)
    
    # return sumEven        # to return value to back to the Thread method, you need to write either Queue or Shared Variable or Custom Thread class

    print(f"Sum of Even elements: {sumEven}")

def SumOfOdd(lst):
    lstOdd = list(filter(CheckOdd, lst))
    sumOdd = reduce(Sum, lstOdd)
    
    #return sumOdd

    print(f"Sum of Odd elements: {sumOdd}")

def main():
    size = int(input("Enter size of list: "))
    lst = list(map(int, input(f"Enter {size} numbers: ").split()))

    T_Even = threading.Thread(target=SumOfEven, args=(lst,))
    T_Odd = threading.Thread(target=SumOfOdd, args=(lst,))

    T_Even.start()
    T_Odd.start()

    T_Even.join()
    T_Odd.join()

if __name__ == "__main__":
    main()
