import numpy as np
import random


class Animal():
    def __init__(self):
        self._gender = random.choice([True, False])
        self._strenght = np.random.randn()

    def direction_to_move(self):
        direction = random.choice([-1, 0, 1])
        return direction


class Bear(Animal):
    def __init__(self):
        super().__init__()
        self._name = 'bear'
    def __str__(self):
        return self._name + str(self._gender) + str(round(self._strenght, 2))


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self._name = 'fish'
    def __str__(self):
        return self._name + str(self._gender) + str(round(self._strenght, 2))

class River():
    def __init__(self, lenght):
        self._river = [
            random.choice([
                None,
                None,
                Bear(),
                Fish(),
            ]) for i in range(lenght)
        ]

    def update(self):
        for i, animal in enumerate(self._river):
            print('previous state', [x.__str__() for x in self._river])
            if animal and i != 0 and i < len(self._river) - 2: # are we still in the river
                direction = animal.direction_to_move()
                print(animal, direction)
                if direction == 0:  # we dont do anything
                    print('---> don\'t really want to move')
                    pass

                else:  # we are moving

                    if self._river[i + direction] is None: # free to move to adjasent place
                        print('---> move to adjesent place')
                        self._river[i] = None
                        self._river[i + direction] = animal

                    elif type(animal) == type(self._river[i + direction]): # same animals meet
                        if animal._gender != self._river[i + direction]._gender: # different geneders
                            print('---> make_babies')
                            idx_none = [i for i, x in enumerate(self._river) if x is None]
                            if not idx_none:
                                self._river[random.choice(idx_none)] = type(animal)()
                        else:
                            print('---> fight')
                            if animal._strenght > self._river[i+direction]._strenght:
                                self._river[i+direction] = animal
                                self._river[i] = None
                            else:
                                self._river[i] = None
                        
                    elif type(animal) != type(self._river[i + direction]):
                        if type(animal) == Fish:
                            print('---> fish moved and died')
                            self._river[i] = None
                        if type(animal) == Bear:
                            print('---> bear moved and eat fish')
                            self._river[i] = None
                            self._river[direction] = animal
            print('next state    ', [x.__str__() for x in self._river], '\n', '-----------------------------')


if __name__ == "__main__":
    b1, b2, = Bear(), Bear()
    print(b1._strenght, b2._strenght, b2._strenght > b1._strenght)
    my_river = River(10)
    print('updating status:', my_river.update())
