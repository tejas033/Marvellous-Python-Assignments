# check if number is prime or not

no1 = int(input("Input: "))
noOfFactors = 0

for i in range (1,no1+1):
    if(no1%i == 0):
        noOfFactors = noOfFactors + 1

if(noOfFactors == 2):
    print("It is Prime Number")
else:
    print("It is Not Prime Number")