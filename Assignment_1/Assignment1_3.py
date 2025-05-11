# Assignment1_3.py

# Create funtion Add() accept two numbers, add them return result

def Add(no1, no2):
    sum = no1 + no2
    return sum

val1 = int(input("Input val1: "))
val2 = int(input("Input val2: "))
result = Add(val1, val2)
print("Output: ", result)