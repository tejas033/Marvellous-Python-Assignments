# Recursion demo 6 sum of 1 to N

def RecursiveSum1ToNo(no, sumCounter):
    if(no >= 0):
        sumCounter += no
        return RecursiveSum1ToNo(no - 1, sumCounter)
    else:
        return sumCounter
    

def main():
    no = int(input('Enter a number to calculate sum of 1 to N = '))
    
    print(f'Sum_n({no}) is: ', RecursiveSum1ToNo(no, 0))

if __name__ == '__main__':
    main()