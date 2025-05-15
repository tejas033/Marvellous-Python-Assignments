# function name = lambda <parameters> : <expression>

CheckEven = lambda No : (No%2 == 0)

val1 = int(input("Input: "))
ret = CheckEven(val1)

if(ret == True):
    print("Even")
else:
    print("Odd")