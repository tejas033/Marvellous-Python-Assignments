# Assignment1_7.py

# Write a function that accepts numbers and check if number is divisible by 5, return true/false

def NumberDivisibleBy5(no1):
    if(no1 % 5 == 0):
        return True
    else:
        return False

value1 = int(input("Input: "))
print("Output: ", NumberDivisibleBy5(value1))