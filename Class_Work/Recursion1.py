# Recursion1.py

def fun():      # callee
    print("Inside fun")

def main():
    fun()   # caller :: main is caller here

if __name__ == "__main__":
    main()