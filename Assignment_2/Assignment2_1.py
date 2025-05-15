# create module > 4 arithmetic methods
# use this module in your python program that takes 2 numbers and pass them to above module methods

from Arithmetic import Add, Sub, Mult, Div

def main():

    no1 = int(input("Input no1: "))
    no2 = int(input("Input no2: "))

    print("Addition is: ",Add(no1, no2))
    print("Subtraction is: ",Sub(no1, no2))
    print("Multiplication is: ",Mult(no1, no2))
    print("Division is: ",Div(no1, no2))

if __name__ == "__main__":
    main()
