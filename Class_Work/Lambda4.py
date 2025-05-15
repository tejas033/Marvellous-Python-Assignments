# function name = lambda <parameters> : <expression>
# CalculateCube :: ** is a "power of" operator

CalculateCube = lambda No : (No**3)

val1 = int(input("1 Input: "))
ret = CalculateCube(val1)

print("1 Cube is: ", ret)

val2 = int(input("2 Input: "))
ret = CalculateCube(val2)

print("2 Cube is: ", ret)