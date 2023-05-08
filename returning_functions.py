"""Returning Functions"""


def math_operation(operation):
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    if operation == '+':
        return add
    elif operation == '-':
        return sub
    else:
        print('Invalid Input')


addition = math_operation('+')
subtraction = math_operation('-')

print('Returning Functions:')
print(addition(5, 7), subtraction(5, 7))


