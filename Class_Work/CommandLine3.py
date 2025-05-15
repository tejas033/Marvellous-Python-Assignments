import sys

def main():
    print("Number of commandline arguments are: ",len(sys.argv))
    print("List of commandline arguments are: ")
    
    i=0
    while(i<len(sys.argv)):
        if(i != 0):
            print(i," Command line argument is: ",sys.argv[i])
        i=i+1

    #for value in sys.argv:
    #    print(value)
    
    for value in range(1,len(sys.argv)):
        print(sys.argv[value])

if __name__ == "__main__":
    main()