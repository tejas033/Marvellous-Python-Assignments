# Recursion7.py

# Print "*" 4 times using recursive function
# Iteration > for loop > while loop > recursion

def Display(no):
    if(no >= 1):
        print("*", end="\t")
        no = no - 1
        Display(no)

def main():
    Display(4)

if __name__ == "__main__":
    main()