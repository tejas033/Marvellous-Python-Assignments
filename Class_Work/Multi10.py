# Multi10.py
# multi processing demo for heavy program

import multiprocessing
import os
import time

def SumEven(no):                    # callback function do not return value
    print("PId of SumEven process is: ", os.getpid())
    print("PPId of SumEven process is: ", os.getppid())
    sumEven = 0
    for i in range (2, no+1, 2):
        sumEven = sumEven + i
    print("Sum of even: ", sumEven)

def SumOdd(no):
    print("PId of SumOdd task is: ", os.getpid())
    print("PPId of SumOdd process is: ", os.getppid())
    sumOdd = 0
    for i in range (1, no+1, 2):
        sumOdd = sumOdd + i
    print("Sum of odd: ", sumOdd)

def main():
    print("Demonstration of Parallel Execution")
    print("PID of main process is: ", os.getpid())      # Process Id of this main process
    print("PPID of main process is: ", os.getppid())       # Process Id of terminal

    start_time = time.time()

    T1 = multiprocessing.Process(target=SumEven, args=(900000000,))
    T2 = multiprocessing.Process(target=SumOdd, args=(900000000,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.time()

    print("Time required for execution is: ", end_time - start_time)

    print("End of main")

if __name__ == "__main__":
    main()