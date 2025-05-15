import sys

def main():
    # pass
    print("Number of commandline arguments are: ",len(sys.argv))
    print("Datatype of argv is: ",type(sys.argv))
    print("First command line argument is: ",sys.argv[0])
    print("2 command line argument is: ",sys.argv[1])
    print("3  command line argument is: ",sys.argv[2])
    print("4 command line argument is: ",sys.argv[3])

if __name__ == "__main__":
    main()