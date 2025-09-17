# Recursion demo 1

# Iterative function to print 1 to N numbers
def IterativeFun(no):
    print('Print numbers using iteration...')

    for i in range(1, no+1):
        print(i, end='\t')

# Recursive function to print 1 to N numbers
def RecursiveFun(no):
    if(no > 0):
        no -= 1
        RecursiveFun(no)
        print(no + 1, end='\t')
        
def main():
    no = int(input('Enter N = '))
    # IterativeFun(no)
    RecursiveFun(no)

if __name__ == '__main__':
    main()