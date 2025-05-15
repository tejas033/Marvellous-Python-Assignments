# print the pattern in numbers

no1 = int(input("Input: "))
cnt = 0

for i in range (1, no1+1):
    for j in range (1, i+1):
        print(j, end="    ")
    print()