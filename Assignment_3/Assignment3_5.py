# Assignment3_5.py

# Sum of Prime numbers in the list

from MarvellousNum import ChkPrime

def ListPrime(lstPrmNumbers):
    sum = 0
    for i in range (len(lstPrmNumbers)):
        sum = sum + lstPrmNumbers[i]
    
    return sum

def main():
    size = int(input("Number of elements: "))
    lstElement = list()
    listPrimeNumber = list()

    print("Input Elements: ")
    for i in range (size):
        lstElement.append(int(input()))
        if ChkPrime(lstElement[i]) == True:
            listPrimeNumber.append(lstElement[i])

    sum = ListPrime(listPrimeNumber)
    print("Output: ", sum)

if __name__ == "__main__":
    main()