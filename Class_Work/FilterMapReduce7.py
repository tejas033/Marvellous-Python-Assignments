# FilterMapReduce7
# custom FMR methods , take user inputs

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

def main():

    Data = []
    print("Enter number of elements: ")
    size = int(input())

    print("Please enter numeric values")

    for i in range(size):
        no = int(input())
        Data.append(no)

    # Data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16]
    print("Input data: ", Data)

    FData = filterX(CheckEven, Data)
    print("Filter output: ", FData)

    MData = mapX(Increase, FData)
    print("Map output: ", MData)

    RData = reduceX(Sum, MData)
    print("Reduce output: ", RData)

if __name__ == "__main__":
    main()
