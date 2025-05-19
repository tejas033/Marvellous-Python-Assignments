# Multi8.py
# sequential heavy program

import threading
import time

def SumEven(no):
    sum = 0
    for i in range (2, no+1, 2):
        sum = sum + i
    print("Sum of even: ", sum)
    return sum

def SumOdd(no):
    sum = 0
    for i in range (1, no+1, 2):
        sum = sum + i
    print("Sum of odd: ", sum)
    return sum

def main():
    print("Demonstration of Sequential Execution")
    start_time = time.time()

    # ret1 = SumEven(90000000)
    # ret2 = SumOdd(90000000)
    # print("Sum of even: ", ret1)
    # print("Sum of odd: ", ret2)
    SumEven(900000000)
    SumOdd(900000000)
    
    end_time = time.time()

    print("Time required for execution is: ", end_time - start_time)

    print("End of main")

if __name__ == "__main__":
    main()