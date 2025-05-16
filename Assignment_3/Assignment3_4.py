# Assignment3_4.py

# frequency of a number in the list

size = int(input("Number of elements: "))
lstElement = list()

print("Input Elements: ")
for i in range (size):
    lstElement.append(int(input()))

print("Element to search: ")
numberToSearch = int(input())
numberOfTimesCounter = 0

for i in range (size):
    if(lstElement[i] == numberToSearch):
        numberOfTimesCounter = numberOfTimesCounter + 1

print("Output: ", numberOfTimesCounter)