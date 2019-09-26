'''Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.'''

import random

def _shuffle(seq):
    shuffled_seq = [0]*(len(seq))
    for value in seq:
        new_index = random.randint(0, (len(seq)-1))
        shuffled_seq[new_index]=value
    return shuffled_seq
print(_shuffle([1,2,3,4,5]))

def shuffle(seq):
# same as the shuffle func of random
    l = []
    while(len(seq) > 0 ):
        r = random.randint(0,len(seq)-1)
        l += [seq[r]]
        del seq[r]
    print(l)
seq = [1,2,3,4]
shuffle(seq)


########   not ok   ################