import re

def get_operators(algebraic_notation):
    return re.findall('\+|\-', algebraic_notation)

def get_expressions(algebraic_notation):
    al_no_spaces = algebraic_notation.replace(' ','')
    expressions_list = re.split('\+|\-', al_no_spaces)
    return expressions_list

#TODO: change to work for more then single digits
def first_derivation(expression):
    if 'x' not in expression:
        return '0'
    elif expression[-1]=='x': #TODO x**1
        return expression.strip('x')
    else:
        coefficient, degree = map(int, expression.split('x**'))
        new_coefficient, new_degree = coefficient*degree, degree-1
        new_expression = str(new_coefficient) + 'x**' + str(new_degree)
        return new_expression


if __name__ == "__main__":
    assert(get_operators('2x**3+4x**2-8x+6')==['+', '-', '+'])
    assert(get_expressions('2x**3+4x**2-8x+6')==['2x**3', '4x**2', '8x', '6'])
    assert(first_derivation('1')=='0')
    assert(first_derivation('5x')=='5')
    print(first_derivation('12x**45'))
    #first_derivative('9x** 3')