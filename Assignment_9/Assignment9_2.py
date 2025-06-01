# Assignment9_2.py

# multiple processes, square numbers in the list

import multiprocessing

def square(no1):
    print(f'Square of {no1} is: {no1 ** 2}')
    
def main():
    
    lst = [1, 2, 3, 4, 5]
    for i in lst:
        mp1 = multiprocessing.Process(target=square, args=(i,))
        mp1.start()
        mp1.join()
    
    print("End of main")

if __name__ == "__main__":
    main()