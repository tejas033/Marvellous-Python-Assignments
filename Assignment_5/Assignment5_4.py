# Assignment5_4.py

# print largest of 3 numbers
# take inputs in single line separated by space
# print variable values in same line 
# new concatination style

no1, no2, no3 = input("Enter three numbers: ").split()
largestNo = 0

if(no1 > no2 and no1 > no3):
    largestNo = no1
elif(no2 > no1 and no2 > no3):
    largestNo = no2
elif(no3 > no1 and no3 > no2):
    largestNo = no3

print(f"Largest number is {largestNo}.")