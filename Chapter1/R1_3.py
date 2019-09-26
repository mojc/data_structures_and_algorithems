def minmax(seq):
    minimum, maximum = seq[0], seq[0]
    for item in seq:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    return minimum, maximum
print(minmax([1,2,5,6,4,77,8,0,4]))
print(minmax([-1, 55, 6.9, -5, -2.7]))