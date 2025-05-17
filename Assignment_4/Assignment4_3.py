# Assignment4_3.py

# Python program to use Filter, Map, Reduce, take "n" numeric elements, 
# Filter numbers between 70 & 90, 
# Map will increase each element by 10
# Reduce will perform multiplication of all the numbers

from functools import reduce

CheckNumberBet70N90 = lambda no : (no >= 70 and no <= 90)
Add10 = lambda no : (no + 10)
ProductOfElements = lambda no1, no2 : (no1 * no2)

print("Enter number of elements: ")
size = int(input())
Data = []

print("Enter list numeric elements: ")
for i in range (size):
    Data.append(int(input()))

FData = list(filter(CheckNumberBet70N90, Data))
print("List after filter: ", FData)

MData = list(map(Add10, FData))
print("List after map: ", MData)

ReduceValue = reduce(ProductOfElements, MData)
print("Output of reduce: ", ReduceValue)