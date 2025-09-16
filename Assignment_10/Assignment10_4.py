# Filter, map, reduce demo.
# User input a list of numbers, filter condition even numbers ; map = number ** 2 ; reduce = sum of all numbers

from functools import reduce

FilterEvenNumbers = lambda no : no % 2 == 0
MapSquareNumber = lambda no : no ** 2
ReduceSum = lambda no1, no2 : no1 + no2

def main():
    # get size of list
    cnt = int(input('Enter number of elements: '))

    lstNumber = []

    # get list of numbers from user
    print(f"Enter numbers for {cnt} times: ")
    for i in range(cnt):
        no = int(input())
        lstNumber.append(no)

    filteredList = list(filter(FilterEvenNumbers, lstNumber))
    print(f'List after filter: {filteredList}')

    mappedList = list(map(MapSquareNumber, filteredList))
    print(f'List after map: {mappedList}')

    reducedSum = reduce(ReduceSum, mappedList)

    print(f'Sum of all the numbers after FMR: {reducedSum}')
    
if __name__ == '__main__':
    main()