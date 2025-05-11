# Assignment1_2.py

# Create funtion ChkNum() and this function should print check if number is EVEN or ODD, print accordingly

def ChkNum(no1):
    if(no1 % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")
    return

value1 = int(input("Input: "))
ChkNum(value1)

# checking type of entered value if it is a String or Number
# print(type(value1))
# if(type(value1) == "<class 'int'>"):
#     ChkNum(value1)
# else:
#     print("Please enter numberic value")
