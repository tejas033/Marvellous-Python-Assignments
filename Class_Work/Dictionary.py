# Dictionary

# Syntax: {key : value}
# Heterogeneous
# Ordered 
# Indexed
# Data Value is mutable
# Duplicate :: key should be unique, value can be overridden

data = {"Name":"Let us C", "Author":"Y Kanetkar", "Price":340, "Publication":"BPB Publication", 0:"asdf"}
print("data type is: ", type(data))
print("len of data: ", len(data))

print("Data 1: ",data)
print("Data Author: ",data["Author"])

data["Price"]=400

print("Data 3: ",data)

#print("Data display using indexed loop")
#for i in range(0, len(data)):
#    print(data[i])

print("Data display using loop")
for value in data:
    print(value)