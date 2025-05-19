# Multi9.py
# multi threading demo for heavy program

import threading
import time

#sumEven = 0
#sumOdd = 0

def SumEven(no):                    # callback function do not return value
    sumEven = 0
    for i in range (2, no+1, 2):
        sumEven = sumEven + i
    print("Sum of even: ", sumEven)

def SumOdd(no):
    sumOdd = 0
    for i in range (1, no+1, 2):
        sumOdd = sumOdd + i
    print("Sum of odd: ", sumOdd)

def main():
    print("Demonstration of Parallel Execution")

    start_time = time.time()

    T1 = threading.Thread(target=SumEven, args=(900000000,))
    T2 = threading.Thread(target=SumOdd, args=(900000000,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.time()

    print("Time required for execution is: ", end_time - start_time)

    print("End of main")

if __name__ == "__main__":
    main()