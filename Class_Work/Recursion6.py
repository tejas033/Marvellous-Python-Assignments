# Recursion6.py

def Display(no):
    # for i in range (no):
    #     print("*", end="\t")

    while(no >= 1):
        print("*", end="\t")
        no = no - 1

def main():
    Display(4)

if __name__ == "__main__":
    main()