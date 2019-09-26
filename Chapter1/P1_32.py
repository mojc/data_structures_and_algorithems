'''Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.'''

def calculator():
    first = float(input('enter fist number:'))
    operator = input('enter the operation:')
    second = float(input('enter second numbre:'))
    if operator == '+':
        return first+second
    elif operator == '-':
        return first-second

    else:
        return 'Unknown operation'

if __name__ == "__main__":
    print(calculator())