# Assignment7_5.py

# Take string input and check if it is palindrome

def isPalindrome(str1):
    reverseStr1 = ""

    for i in range (len(str1) - 1, -1, -1):
        reverseStr1 = reverseStr1 + str1[i]
    
    if(str1 == reverseStr1):
        print(f"{str1} is a palindrome.")
        return True
    else:
        print(f"{str1} is not a palindrome.")
        return False

def main():
    str = input("Enter a string: ")
    isPalindrome(str)

if __name__ == "__main__":
    main()