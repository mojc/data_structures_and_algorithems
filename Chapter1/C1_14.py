def distinct_odd_pair(seq):
    '''Write a short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd.'''
    count_odd = 0
    for number in seq:
        if number%2==1:
            count_odd+=1
    return count_odd%2==0

print(distinct_odd_pair([2,2,3,4,5]))
print(distinct_odd_pair([2,2,4,4,5]))