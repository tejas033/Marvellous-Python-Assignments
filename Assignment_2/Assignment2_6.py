# print the pattern

no1 = int(input("Input: "))

for i in range (0, no1):
    for j in range (no1 - i, 0, -1):
        print("*", end="    ")
    print()