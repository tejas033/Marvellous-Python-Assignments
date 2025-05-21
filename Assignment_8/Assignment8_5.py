# Assignment8_5.py

# Using multi-threading display 1 to 50 using T1 and 50 to 1 using T2. T2 should start execution after T1 is completed

import threading

def PrintNumbers(fromNo, toNo, step):
    print("", [i for i in range (fromNo, toNo, step)])

def main():
    thread1 = threading.Thread(target = PrintNumbers, args=(1, 51, 1))
    thread1.start()
    thread1.join()

    thread2 = threading.Thread(target = PrintNumbers, args=(50, 0, -1))
    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()