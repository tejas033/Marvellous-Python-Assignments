# Recursion8.py

# Input: 4 ... Output: 4+3+2+1
# Iteration > for loop > while loop > recursion

sum = 0
factorial = 1

def AddRecursion(no):
    global sum
    if(no >= 1):
        sum = sum + no
        no = no - 1
        AddRecursion(no)

def FactorialWhile(no):
    fact = 1
    while(no >= 1):
        fact = fact * no
        no = no - 1
    
    return fact

def FactorialRecursion(no):
    global factorial
    if(no >= 1):
        factorial = factorial * no
        no = no - 1
        FactorialRecursion(no)
    
    return factorial

def main():
    AddRecursion(4)
    print("Sum: ", sum)

    fact = FactorialWhile(4)
    print("FactorialWhile: ", fact)

    factRecur = FactorialRecursion(4)
    print("FactorialRecursion: ", factRecur)

if __name__ == "__main__":
    main()