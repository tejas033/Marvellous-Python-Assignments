# write a program to calculate factorial

no1 = int(input("Input: "))
factorial = 1

for i in range (1,no1):
    factorial = factorial * (i + 1)

print("Output: ", factorial)