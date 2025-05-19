# Assignment5_3.py

# Voting eligitility criteria

try:
    age = int(input("Enter age: "))
    if(age >= 18):
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote.")
except Exception as objExcep:
    print("Exception occurred, expected input should be numeric value: ", objExcep)