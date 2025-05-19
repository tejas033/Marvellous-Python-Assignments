# Multi7.py
# Multi-threading demo 4

import threading

def Display(val1, val2):
    print("Inside Display val: ",val1, val2)
    print("Thread ID of child thread is: ", threading.get_ident())
    for i in range (10):
        print(i)

def main():
    print("Inside Main")
    print("Thread ID of main is: ", threading.get_ident())
    T1 = threading.Thread(target = Display, args=(11,21))       
    T1.start()
    T1.join()           # wait until child thread is completed

    print("End of main")

if __name__ == "__main__":
    main()