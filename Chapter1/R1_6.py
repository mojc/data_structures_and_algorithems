def sum_odd_squares(n):
    return sum(n**2 for n in range(n) if n%2==1)
'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''
if __name__ == "__main__":
    print(sum_odd_squares(6))