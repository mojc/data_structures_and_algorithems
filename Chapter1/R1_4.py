def sum_positive_squares(n):
    '''Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.'''
    assert n > 0
    return sum(n**2 for n in range(n))

if __name__ == "__main__":
    print(sum_positive_squares(5))
    print(sum_positive_squares(19))
    print(sum_positive_squares(-5))