# Recursion5.py

# Recursion limit :: getrecursionlimit & setrecursionlimit

import sys

def main():
    print("1 :: ", sys.getrecursionlimit())
    sys.setrecursionlimit(2000)
    print("2 :: ", sys.getrecursionlimit())

if __name__ == "__main__":
    main()