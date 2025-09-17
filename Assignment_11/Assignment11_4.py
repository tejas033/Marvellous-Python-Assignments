# Recursion demo 4 power or exponential function using recursion

def RecursivePowerCalculation(no, cntIterations):
    if cntIterations == 1:
        return no
    else:
        cntIterations -= 1
        return no * RecursivePowerCalculation(no, cntIterations)


def main():
    no = int(input('Enter a number = '))
    pow = int(input('Enter power = '))
    
    print(f'power of ({no}, {pow}) -> ', RecursivePowerCalculation(no, pow))

if __name__ == '__main__':
    main()