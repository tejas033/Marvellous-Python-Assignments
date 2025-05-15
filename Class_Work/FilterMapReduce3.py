# FilterMapReduce3
# Filter :: even numbers, Map :: add 1 to the number, Reduce :: sum of these numbers

from functools import reduce

Data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16]
print("Input data: ", Data)

# FData = list(filter(lambda No : (No%2 == 0), Data))
# print("Filter output: ", FData)

# MData = list(map(lambda No : (No+1), FData))
# print("Map output: ", MData)

# RData = reduce(lambda A, B : (A+B),MData)
# print("Reduce output: ", RData)

RData = reduce(lambda A, B : (A+B),list(map(lambda No : (No+1), list(filter(lambda No : (No%2 == 0), Data)))))
print("Reduce output: ", RData)