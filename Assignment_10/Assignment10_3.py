# Filter, map, reduce demo.
# User input a list of numbers, filter condition number >= 70 && number <= 90 ; map = number + 10 ; reduce = product of all numbers

from functools import reduce

FilterNoBetween70And90 = lambda no : no >= 70 and no <= 90    
MapIncreaseNo10 = lambda no : no + 10
ReduceMultiple = lambda no1, no2 : no1 * no2

def main():
    # get size of list
    cnt = int(input('Enter number of elements: '))

    lstNumber = []

    # get list of numbers from user
    print(f"Enter numbers for {cnt} times: ")
    for i in range(cnt):
        no = int(input())
        lstNumber.append(no)

    # print(lstNumber)

    filteredList = list(filter(FilterNoBetween70And90, lstNumber))
    print(f'List after filter: {filteredList}')

    mappedList = list(map(MapIncreaseNo10, filteredList))
    print(f'List after map: {mappedList}')

    reducedMultiplication = reduce(ReduceMultiple, mappedList)

    print(f'Multiplication of all the numbers after FMR: {reducedMultiplication}')
    
if __name__ == '__main__':
    main()