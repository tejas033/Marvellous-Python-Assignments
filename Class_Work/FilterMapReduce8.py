# FilterMapReduce8
# custom FMR methods , take user inputs

# our own Module

from MarvellousFMR import filterX, mapX, reduceX

CheckEven = lambda No : (No%2 == 0)
Increase = lambda No : (No+1)
Sum = lambda A, B : (A+B)

def main():

    Data = []
    print("Enter number of elements: ")
    size = int(input())

    print("Please enter numeric values")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input data: ", Data)

    FData = filterX(CheckEven, Data)
    print("Filter output: ", FData)

    MData = mapX(Increase, FData)
    print("Map output: ", MData)

    RData = reduceX(Sum, MData)
    print("Reduce output: ", RData)

if __name__ == "__main__":
    main()
