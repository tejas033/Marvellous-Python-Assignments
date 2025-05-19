# Recursion3.py


def fun():
    i = 0
    print("Inside fun: ", i)
    i = i + 1
    fun()       # RecursionError: maximum recursion depth exceeded,  [Previous line repeated 995 more times]

def main():
    fun()

if __name__ == "__main__":
    main()