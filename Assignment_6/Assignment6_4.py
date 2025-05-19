# Assignment6_4.py

# Factorial of a number using for loop

def main():
    no1 = int(input("Enter a number: "))
    fact = 1;
    for i in range (2, no1+1):
        fact = fact * i
    print(f"Factorial of {no1} is: {fact}")

if __name__ == "__main__":
    main()