# Assignment6_5.py

# check if number is prime or not

import math

no1 = int(input("Enter a number: "))

# divisibleCnt = 0
# for i in range (2, int(no1/2) + 1):        # Time complexity is O(n/2)
#     if(no1 % i == 0):
#         divisibleCnt = divisibleCnt + 1

# if(divisibleCnt == 0 and no1 != 1 and no1 != 0):        # Prime number is divisible by exactly 2 numbers: 1 and itself
#     print(f"{no1} is a prime number.")
# else:
#     print(f"{no1} is not a prime number.")

def isPrime(no1):
    for i in range (2, int(math.sqrt(no1)) + 1):        # Time complexity is O(sqrt of no1)
        if(no1 % i == 0):
            return False
    return True
        
if(isPrime(no1) and no1 != 0):
    print(f"{no1} is a prime number.")
else:
    print(f"{no1} is not a prime number.")