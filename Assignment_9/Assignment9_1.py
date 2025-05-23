# Assignment9_1.py

# print numbers 1 to 5, 3 times using multi-threading, each print after delay of 1 sec

import threading
import time

def printNumbers(no1, no2, strThreadName):
    print("Thread name: ", strThreadName)
    for i in range (no1, no2+1):
        print(i, end="  ")
    print()
    
def main():
    T1 = threading.Thread(target=printNumbers, args=(1, 5, 'T1'))
    T2 = threading.Thread(target=printNumbers, args=(1, 5, 'T2'))
    T3 = threading.Thread(target=printNumbers, args=(1, 5, 'T3'))

    T1.start()
    time.sleep(1)
    T2.start()
    time.sleep(1)
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("End of main")

if __name__ == "__main__":
    main()
