# Recursion2.py

def fun():      # callee
    print("Inside fun")
    fun()       # RecursionError: maximum recursion depth exceeded,  [Previous line repeated 995 more times]

def main():
    fun()   # caller :: main is caller here

if __name__ == "__main__":
    main()