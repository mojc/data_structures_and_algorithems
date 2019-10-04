import re


# TODO: make it more classy
def get_operators(algebraic_notation):
    operators = re.findall('\+|\-', algebraic_notation)
    if operators[0] == '+':
        operators = ['+'] + operators
    return operators


def get_expressions(algebraic_notation):
    al_no_spaces = algebraic_notation.replace(' ', '')
    expressions_list = re.split('\+|\-', al_no_spaces)
    if expressions_list[0] == '':
        expressions_list=expressions_list[1:]
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
    expressions = get_expressions(algebraic_notation)
    result = 'y='
    for expresion, operator in zip(expressions, operators):
        result = result + operator + first_derivation(expresion)
    return result


if __name__ == "__main__":
    assert(get_operators('2x**3+4x**2-8x+6') == ['+', '+', '-', '+'])
    assert(get_operators('-2x**3+4x**2-8x+6') == ['-', '+', '-', '+'])
    assert(get_expressions('2x**3+4x**2-8x+6') == ['2x**3', '4x**2', '8x', '6'])
    assert(first_derivation('6') == '0')
    assert(first_derivation('5x') == '5')
    assert(first_derivation_of_poly('2x**3+4x**2-8x+6') == 'y=+6x**2+8x**1-8+0')
    assert(first_derivation_of_poly('-4x**4+4x**2-8x+6') == 'y=-16x**3+8x**1-8+0')
