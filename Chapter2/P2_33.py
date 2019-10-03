import re


# TODO: doesn't work with negative numbers
def get_operators(algebraic_notation):
    return re.findall('\+|\-', algebraic_notation)


def get_expressions(algebraic_notation):
    al_no_spaces = algebraic_notation.replace(' ', '')
    expressions_list = re.split('\+|\-', al_no_spaces)
    return expressions_list


def first_derivation(expression):
    if 'x' not in expression:
        return '0'
    elif expression[-1] == 'x':  # TODO x**1
        return expression.strip('x')
    else:
        coefficient, degree = map(int, expression.split('x**'))
        new_coefficient, new_degree = coefficient*degree, degree-1
        new_expression = str(new_coefficient) + 'x**' + str(new_degree)
        return new_expression


def first_derivation_of_poly(algebraic_notation):
    operators = get_operators(algebraic_notation)
    operators.append('')
    expressions = get_expressions(algebraic_notation)
    result = 'y='
    for expresion, operator in zip(expressions, operators):
        result = result + first_derivation(expresion) + operator
    return result


if __name__ == "__main__":
    assert(get_operators('2x**3+4x**2-8x+6') == ['+', '-', '+'])
    assert(get_expressions('2x**3+4x**2-8x+6') == ['2x**3', '4x**2', '8x', '6'])
    assert(first_derivation('6') == '0')
    assert(first_derivation('5x') == '5')
    assert(first_derivation_of_poly('2x**3+4x**2-8x+6') == 'y=6x**2+8x**1-8+0')
