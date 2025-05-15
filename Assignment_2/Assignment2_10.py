# print the sum of digits in a number

no1 = input("Input: ")
length = len(no1)
sum = 0

for i in range (length):
    print("i: ",i)
    sum = sum + int(no1[i])

print("Output: ", sum)