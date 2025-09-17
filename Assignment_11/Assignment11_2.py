# Recursion demo 2 Factorial

facto = 1

def RecursiveFactorial(no):
    if(no > 1):
        # Recursive Factorial with global variable

        # no -= 1
        # RecursiveFactorial(no)
        # global facto 
        # facto = facto * (no + 1)

        # Recursive Factorial without global variable

        return no * RecursiveFactorial(no - 1)
    else:
        return 1

def main():
    no = int(input('Enter N to calculate factorial of = '))
    
    print(f'factorial({no}) -> ', RecursiveFactorial(no))

    # iterative factorial ... 
    # facto = 1
    # for i in range(1, no + 1):
    #     facto = facto * i
    # print(facto)

if __name__ == '__main__':
    main()