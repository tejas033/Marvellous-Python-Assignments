# FilterMapReduce5

# pass function as parameter
# call back method prototype

def Increase(A):
    return A+1

def Demo(Task, Value):
    MData = []
    
    for no in Value:
        MData.append(Task(no))
    
    return MData

Data = [13, 17, 10, 14, 11]

RData = list(Demo(Increase, Data))
print(RData)

Sum = 0
for i in RData:
    Sum = Sum + i

print(Sum)