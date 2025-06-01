# Assignment9_3.py

# multiple cores, square numbers in the list

import multiprocessing.pool

def factorial(no1):
    fact = 1;
    for i in range (no1, 0, -1):
        fact = fact * i
    print(f'Factorial of {no1} is: {fact}')

    return fact

    
def main():
    
    lst = [1, 2, 3, 4, 5]
    multiPool = multiprocessing.Pool()
    result = multiPool.map(factorial, lst)
    
    multiPool.close()
    multiPool.join()

    print(result)
    
    print("End of main")

if __name__ == "__main__":
    main()