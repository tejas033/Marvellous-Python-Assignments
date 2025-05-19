# Assignment5_2.py

# Take single character from user, check if it is vowel or consonent

def CheckIfVowel(char1):
    tupleVowel = ('a', 'e', 'i', 'o', 'u')
    if(char1 in tupleVowel):
        print("'" + char1 + "' is a vowel.")
    else:
        print("'" + char1 + "' is not a vowel.")

def main():
    print("Enter a character: ", end=" ")
    char1 = input()
    CheckIfVowel(char1)

if __name__ == "__main__":
    main()