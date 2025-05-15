def main():
    print("Enter number of elements: ")
    size = int(input())

    data = list()

    print("Enter the values :: ")
    for i in range(size):
        no = int(input())
        data.append(no)

    sum=0
    print("Entered elements are: ")
    for value in data:
        print("-> value: ",value)
        sum = sum + value

    print("Sum is: ",sum)

if __name__ == "__main__":
    main()