# Lambda function to take 2 parameters and return multiplication of both

Multiplication = lambda no1, no2 : no1 * no2

val1 = int(input('Enter first number: '))
val2 = int(input('Enter second number: '))

print(f'Multiplication of {val1} & {val2} is: {Multiplication(val1, val2)}')