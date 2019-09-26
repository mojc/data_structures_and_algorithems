'''The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5, 10, 15, 20, . . . , 100.'''

import random



def bday_paradox(number_of_people, trials=100):
    def is_bday(number_of_people):
        bdays = [random.randint(1,356) for i in range(number_of_people)]
        if len(bdays) > len(set(bdays)):
            return True
        else: return False

    success=0
    for _ in range(trials):
        if is_bday(number_of_people):
            success+=1
    return success/trials

print([bday_paradox(n) for n in range(1,100,5)])
print(bday_paradox(23))
