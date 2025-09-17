# While writing recursion logic keep following items in mind:
# 1. call to the method in the same method
# 2. next iteration value should be passed via call to same method
# 3. breaking condition or the last iteration condition should return last value

# Recursion demo 3 Sum of digits

def RecursiveSumOfDigits(no):
    # print(no)

    if no != 0:
        # print(f'return: (no % 10) {(no % 10)} + int(no / 10) {int(no / 10)}')
        return (no % 10) + RecursiveSumOfDigits( int(no / 10) )
    else:
        return 0

def main():
    no = int(input('Enter a number to calculate sum of digits = '))
    
    print(f'sum_of_digits({no}) -> ', RecursiveSumOfDigits(no))

if __name__ == '__main__':
    main()