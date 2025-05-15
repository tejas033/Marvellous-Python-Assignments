# write a program to calculate Sum of factors of a number

no1 = int(input("Input: "))
factors = 1
sum = 0

for i in range (1,no1):
    if(no1%i == 0):
        sum = sum + i

print("Output: ", sum)