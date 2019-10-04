import numpy as np
import random


class Animal():
    def __init__(self):
        pass

    def direction_to_move(self):
        direction = np.random.randint(-1, 2)
        return direction


class Bear(Animal):
    def __init__(self):
        self._name = 'bear'


class Fish(Animal):
    def __init__(self):
        self._name = 'fish'


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
            if animal and i != 0 and i < len(self._river) - 2:
                direction = animal.direction_to_move()
                if direction == 0:  # we dont do anything
                    pass
                else:  # we are moving
                    if self._river[i + direction] is None:
                        print('move to adjesent place')
                        print('previsou state:', self._river)
                        self._river[i] = None
                        self._river[i + direction] = animal
                        print('next state:', self._river)
                    elif type(animal) == type(self._river[i + direction]):
                        type(animal)()
                        print('make_babies')
                    elif type(animal) != type(self._river[i + direction]):
                        print('bear kills fish')
                        if type(animal) == Fish:
                            self._river[i] = None
                        if type(animal) == Bear:
                            self._river[i] = None
                            self._river[-1] = animal


if __name__ == "__main__":
    my_river = River(10)
    print('updating status:', my_river.update())
