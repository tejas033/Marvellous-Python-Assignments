# Tuple  :: Constant

# Syntax: ()
# Heterogeneous
# Ordered 
# Indexed
# Data is NOT mutable
# Duplicate allowed

data = (10,90.67,"hello",40,True, 40)
print("data type is: ", type(data))
print("len of data: ", len(data))

print(data)
print(data[0])
print(data[1])

# data[0] = 11          Tuple data is immutable
# data.append(40)

print('at 5: ',data[5])

print("Data display using loop")
for value in data:
    print(value)

print("Data display using indexed loop")
for i in range(0, len(data)):
    print(data[i])