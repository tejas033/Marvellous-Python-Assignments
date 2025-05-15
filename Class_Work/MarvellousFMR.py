# MarvellousFMR.py

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