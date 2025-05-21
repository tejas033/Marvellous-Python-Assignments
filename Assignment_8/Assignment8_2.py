# Assignment8_1.py

# Multi-threading program to perform sum of EvenFactor and OddFactor of a number

import threading

def SumOfEvenFactors(no):
    if(no % 2 == 0):
        sumOfEven = no
    else:
        sumOfEven = 0

    # for i in range (1, no+1):                 # O(n)
    #     if(no % i == 0 and i % 2 == 0):
    #         sumOfEven = sumOfEven + i

    for i in range (1, int(no / 2) + 1):        # O(n/2 + 1)
        if(no % i == 0 and i % 2 == 0):
            sumOfEven = sumOfEven + i

    print(f"Sum of Even Factors of {no} is: {sumOfEven}")

def SumOfOddFactors(no):
    if(no % 2 != 0):
        sumOfOdd = no
    else:
        sumOfOdd = 0
    
    # for i in range (1, no+1):
    #     if(no % i == 0 and i % 2 != 0):
    #         sumOfOdd = sumOfOdd + i

    for i in range (1, int(no / 2) + 1):
        if(no % i == 0 and i % 2 != 0):
            sumOfOdd = sumOfOdd + i

    print(f"Sum of Odd Factors of {no} is: {sumOfOdd}")

def main():
    no1 = int(input("Enter no1: "))

    T1 = threading.Thread(target=SumOfEvenFactors, args=(no1,))
    T2 = threading.Thread(target=SumOfOddFactors, args=(no1,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    print("exit from main")

if __name__ == "__main__":
    main()
