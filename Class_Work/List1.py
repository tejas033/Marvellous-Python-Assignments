# List

# Syntax: []
# Heterogeneous
# Ordered 
# Indexed
# Data is mutable
# List is mutable
# Duplicate allowed

data = [10,90.67,"hello",40,True]
print("data type is: ", type(data))
print("len of data: ", len(data))

print(data)

print(data[0])
print(data[1])
print(data[2])
print(data[3])

data[0] = 11

print(data[0])

data.append(40)
print('at 4: ',data[4])

print("Data display using loop")
for value in data:
    print(value)