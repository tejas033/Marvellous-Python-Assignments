# Assignment3_3.py
# Read N numbers, store them in list, get smallest number

size = int(input("Number of elements: "))
lstElement = list()
numberSmallest = 0

print("Input Elements: ")
for i in range (size):
    lstElement.append(int(input()))
    if(lstElement[i] < numberSmallest):
        numberSmallest = lstElement[i]

# for i in range (size):
#     if(lstElement[i] < numberSmallest):
#         numberSmallest = lstElement[i]

print("Output: ", numberSmallest)