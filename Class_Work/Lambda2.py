def CheckEven(No):
    return (No%2 == 0)

val1 = int(input("Input: "))
ret = CheckEven(val1)

if(ret == True):
    print("Even")
else:
    print("Odd")