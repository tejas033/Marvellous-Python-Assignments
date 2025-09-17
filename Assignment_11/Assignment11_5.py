# Recursion demo 5 count number of zeros in the given number
# this program does not work for number having only zeros ... 

# zeroCnt = 0

def RecursiveCountZero(no, zeroCounter):
    remainder = no % 10
    division = int(no / 10)

    if no != 0:
        if(remainder == 0):
            zeroCounter += 1
            # global zeroCnt
            # zeroCnt += 1
        return RecursiveCountZero(division, zeroCounter)
    else:
        return zeroCounter          # at last return the zeroCounter .. this is without using global variable

def main():
    no = int(input('Enter a number that may contain zero = '))
    
    print(f'number of zeros in {no} are: ', RecursiveCountZero(no, 0))

if __name__ == '__main__':
    main()