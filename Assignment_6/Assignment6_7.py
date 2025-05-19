# Assignment6_7.py

# accept 5 numbers from user, find the greatest number

print("Enter 5 numbers: ")
lstNumbers = []
# lstNumbers = input().split()
# largestNo = int(lstNumbers[0])

# for i in range (0, 5):
#     if(largestNo < int(lstNumbers[i])):
#         largestNo = int(lstNumbers[i])

lstNumbers = list(map(int, input().split()))
largestNo = lstNumbers[0]

for i in range (0, 5):
    if(largestNo < lstNumbers[i]):
        largestNo = lstNumbers[i]

print("Maximum number is:", largestNo)