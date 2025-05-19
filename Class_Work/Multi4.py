# Multi4.py
# Multi-threading demo

import threading

def Display():
    print("Inside Display")

def main():
    print("Inside Main")
    T1 = threading.Thread(target=Display)       # create thread
    T1.start()                                  # move thread to runnable

    print("T1: ", T1)

if __name__ == "__main__":
    main()