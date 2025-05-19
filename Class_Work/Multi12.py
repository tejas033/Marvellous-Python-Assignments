# Multi12.py
# Multi Core-programming

import os

def fun(no):
    sum = 0
    for i in range (1,no):
        sum = sum + (i*i*i)
    
    return sum

def main():
    val1 = fun(1000)

    print(val1)

if __name__ == "__main__":
    main()