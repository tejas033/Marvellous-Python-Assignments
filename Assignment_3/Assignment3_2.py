# Assignment3_2.py
# Read N numbers, store them in list, get largest number

size = int(input("Number of elements: "))
lstElement = list()
numberLargest = 0

print("Input Elements: ")
for i in range (size):
    lstElement.append(int(input()))
    if(i == 1):
        numberLargest = lstElement[i]
    
    if(lstElement[i] > numberLargest):
        numberLargest = lstElement[i]

# for i in range (size):
#     if(i == 1):
#         numberLargest = lstElement[i]
    
#     if(lstElement[i] > numberLargest):
#         numberLargest = lstElement[i]

print("Output: ", numberLargest)