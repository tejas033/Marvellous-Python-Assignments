# Assignment8_4.py

# Count number of small and capital letters and digits in the provided string

import threading

def SmallChars(str):
    smallCharCnt = 0

    for char in str:
        if(char >= 'a' and char <= 'z'):
            smallCharCnt = smallCharCnt + 1

    print("Number of Small characters are:", smallCharCnt)

def CapitalChars(str):
    capitalCharCnt = 0

    for char in str:
        if(char >= 'A' and char <= 'Z'):
            capitalCharCnt = capitalCharCnt + 1

    print("Number of Capital characters are:", capitalCharCnt)

def Digits(str):
    digitCnt = 0

    for digit in str:
        if(digit >= '0' and digit <= '9'):
            digitCnt = digitCnt + 1

    print("Number of digits are:", digitCnt)

# def CountCharacters(str):
#     smallCharCnt = 0
#     capitalCharCnt = 0
#     digitCnt = 0

#     for letter in str:
#         if(letter >= 'a' and letter <= 'z'):
#             smallCharCnt = smallCharCnt + 1
        
#         elif(letter >= 'A' and letter <= 'Z'):
#             capitalCharCnt = capitalCharCnt + 1
        
#         elif(letter >= '0' and letter <= '9'):
#             digitCnt = digitCnt + 1

#     print("Number of Small characters are:", smallCharCnt)
#     print("Number of Capital characters are:", capitalCharCnt)
#     print("Number of Digits are:", digitCnt)

def main():
    str1 = input("Enter string: ")
    
    print()

    t_small     = threading.Thread(target=SmallChars, args=(str1,))
    t_capital   = threading.Thread(target=CapitalChars, args=(str1,))
    t_digit     = threading.Thread(target=Digits, args=(str1,))

    t_small.start()
    t_capital.start()
    t_digit.start()

    t_small.join()
    t_capital.join()
    t_digit.join()

    print()

    print(f"Small Char Thread Name: {t_small.name} , Id: {t_small.ident}")
    print(f"Capital Char Thread Name: {t_capital.name} , Id: {t_capital.ident}")
    print(f"Digit Thread Name: {t_digit.name} , Id: {t_digit.ident}")

if __name__ == "__main__":
    main()