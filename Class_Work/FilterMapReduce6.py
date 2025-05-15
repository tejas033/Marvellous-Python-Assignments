# FilterMapReduce6

# custom FMR methods

CheckEven = lambda No : (No%2 == 0)
Increase = lambda No : (No+1)
Sum = lambda A, B : (A+B)

def filterX(Task, Value):
    lst = []
    for i in Value:
        if(Task(i) == True):
            lst.append(i)
    
    return lst

def mapX(Task, Value):
    lst = []
    for i in Value:
        lst.append(Task(i))
    
    return lst

def reduceX(Task, Value):
    Result = 0
    for i in Value:
        Result = Task(Result, i)
    
    return Result

Data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16]
print("Input data: ", Data)

FData = filterX(CheckEven, Data)
print("Filter output: ", FData)

MData = mapX(Increase, FData)
print("Map output: ", MData)

RData = reduceX(Sum, MData)
print("Reduce output: ", RData)