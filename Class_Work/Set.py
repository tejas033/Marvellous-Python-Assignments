# Set

# Syntax: {}
# Heterogeneous
# NOT Ordered 
# NOT Indexed
# Data is NOT mutable
# Set is mutable
# Duplicate NOT allowed

data = {10,90.67,"hello",40,True,10}
print("data type is: ", type(data))
print("len of data: ", len(data))

print("Data 1: ",data)
print("Data 2: ",data)
# print(data[0])        # Index is not allowed for Set

# data[0] = 11
data.add(99)
data.add(98)
if(data.__contains__(40)):
    data.remove(40)

# print('at 5: ',data[5])   # data is not subscriptable

print("Data 3: ",data)

#print("Data display using indexed loop")
#for i in range(0, len(data)):
#    print(data[i])

print("Data display using loop")
for value in data:
    print(value)
