import sys

def Addition(no1,no2):
    Ans = 0
    Ans = no1 + no2
    return Ans

def main():
    if(len(sys.argv) != 3):
        print("Insufficient number of arguments")
        return

    value1 = 0
    value2 = 0

    #if(len(sys.argv) >= 3):
    #    value1 = int(sys.argv[1])
    #    value2 = int(sys.argv[2])

    for value in range(1,len(sys.argv)):
        if(value == 1):
            value1 = int(sys.argv[value])
        if(value == 2):
            value2 = int(sys.argv[value])

    Result = Addition(value1, value2)

    print("Addition is: ",Result)

if __name__ == "__main__":
    main()