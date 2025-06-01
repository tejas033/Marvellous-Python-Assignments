# Assignment9_4.py

# sum of 1 to 10 millions using normal function, threading, 

import multiprocessing.pool
import threading
import time

def sum(startNo, endNo):
    sum = 0
    for i in range (startNo, endNo + 1):
        sum = sum + i

    return sum
    
def main():
    start_time = time.time()
    total = sum(1, 10000)
    end_time = time.time()

    print('Total of 1 to 10 million is: ', total)
    print('Time required using regular function is: ', end_time - start_time)

    start_time = time.time()
    T1 = threading.Thread(target = sum, args = (1, 10000))
    T1.start()
    T1.join()
    end_time = time.time()
    print('Time required using multi-threading function is: ', end_time - start_time)

    start_time = time.time()
    T1 = multiprocessing.Process(target = sum, args = (1, 10000))
    T1.start()
    T1.join()
    end_time = time.time()
    print('Time required using multi-processing function is: ', end_time - start_time)
    
    print("End of main")

if __name__ == "__main__":
    main()