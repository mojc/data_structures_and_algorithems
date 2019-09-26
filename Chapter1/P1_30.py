'''Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.'''

def two_divisions(number):
    assert number>2
    i=0
    while number/2>2:
        i+=1
        number = number/2
    print(number,i)

#could be done with log of 2
print(two_divisions(22))
print(two_divisions(10))
print(two_divisions(2200000))
print(two_divisions(22.3))
print(two_divisions(2))