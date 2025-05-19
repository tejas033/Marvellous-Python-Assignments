# Multi6.py
# Multi-threading demo 3

import threading

def Display(val1, val2):
    print("Inside Display val: ",val1, val2)
    for i in range (1000):
        print(i)

def main():
    print("Inside Main")
    T1 = threading.Thread(target = Display, args=(11,21))       
    T1.start()                                                  

    print("End of main")

if __name__ == "__main__":
    main()