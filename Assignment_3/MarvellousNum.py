# This is MarvellousNum module

import math

def ChkPrime(number):
    for i in range (2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            return False
    return True