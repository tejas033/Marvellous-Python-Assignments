# Filter, map, reduce demo.
# User input a list of numbers, filter prime numbers ; map = number * 2 ; reduce = largest number of list

from functools import reduce

def FilterPrimeNumber(no):
    n = int(no/2)+1
    for i in range(2, n):
        if(no != 2 and no % i == 0):
            return False
    
    return True
        
MapDoubleNumber = lambda no : no * 2

def ReduceLargest(no1, no2):
    if(no1 >= no2):
        return no1
    else:
        return no2

def main():
    # get size of list
    cnt = int(input('Enter number of elements: '))

    lstNumber = []

    # get list of numbers from user
    print(f"Enter numbers for {cnt} times: ")
    for i in range(cnt):
        no = int(input())
        lstNumber.append(no)

    filteredList = list(filter(FilterPrimeNumber, lstNumber))
    print(f'List after filter: {filteredList}')

    mappedList = list(map(MapDoubleNumber, filteredList))
    print(f'List after map: {mappedList}')


    if(len(mappedList) != 0):
        reducedLargestNumber = reduce(ReduceLargest, mappedList)
        print(f'Largest of all the numbers after FMR: {reducedLargestNumber}')
    else:
        print('No prime number present')
    
if __name__ == '__main__':
    main()