# print the pattern in numbers

no1 = int(input("Input: "))

for i in range (0, no1):
    for j in range (1, no1+1):
        print(j, end="    ")
    print()