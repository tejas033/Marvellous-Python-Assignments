# take "n" numbers, store them in list, return sum of all numbers

size = int(input("Enter number of elements: "))
lstElements = list()

sum = 0
print("Input Elements: ")
for i in range (size):
    lstElements.append(int(input()))
    sum = sum + lstElements[i]

print("Output: ", sum)
