# Lambda function demo to take 1 parameter and return square of that number

Square = lambda number : number ** 2

val1 = int(input('Enter a number: '))
print(f'Square of {val1} is: {Square(val1)}')