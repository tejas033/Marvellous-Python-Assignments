# Multi5.py
# Multi-threading demo 2

import threading

def Display(val1, val2):
    print("Inside Display val1: ",val1)
    print("Inside Display val2: ",val2)

def main():
    print("Inside Main")
    T1 = threading.Thread(target = Display, args=(11,21))       # create thread
    T1.start()                                                  # move thread to runnable

    print("T1: ", T1)

if __name__ == "__main__":
    main()