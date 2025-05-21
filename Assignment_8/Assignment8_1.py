# Assignment8_1.py

# Multi-threading to display first 10 even and odd numbers

import threading

def DisplayEven(no1):
    print(f"First {no1} even numbers are: ")

    i=0
    intEvenNo = 0
    while i < no1:
        if(intEvenNo % 2 == 0):
            print(intEvenNo, end="  ")
            i = i + 1
        intEvenNo = intEvenNo + 1

    print()

def DisplayOdd(no1):
    print(f"First {no1} odd numbers are: ")

    i = 0
    cntNumbers = 0
    while i < no1:
        if(cntNumbers % 2 != 0):
            print(cntNumbers, end="  ")
            i = i + 1
        cntNumbers = cntNumbers + 1
    print()
    
def main():
    T1 = threading.Thread(target=DisplayEven, args=(10,))
    T2 = threading.Thread(target=DisplayOdd, args=(10,))

    T1.start()
    T2.start()

if __name__ == "__main__":
    main()
