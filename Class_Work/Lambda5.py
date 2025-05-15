# def Power(No, Pow):
#     Res = 1

#     for i in range (Pow):           # time complexity > O(Pow)
#         Res = Res * No

#     return Res

# above Power method can be reduced using lambda function

Power = lambda No, Pow : (No ** Pow)

val1 = int(input("Input Number: "))
val2 = int(input("Input Power: "))

ret = Power(val1, val2)

print("Power raise to: ", ret)