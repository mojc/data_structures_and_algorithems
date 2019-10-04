import numpy as np
import random


class Animal():
    def __init__(self):
        pass

    def direction_to_move(self):
        direction = np.random.randint(-1,2)
        return direction

class Bear(Animal):
    def __init__(self):
        self._name = 'bear'

class Fish(Animal):
    def __init__(self):
        self._name = 'fish'


class River():
    def __init__(self, lenght):
        self._river = [random.choice([None, None, Bear(), Fish(),]) for i in range(lenght)]
    
    def update(self):
        for i, animal in enumerate(self._river):
            print((animal))
            if animal:
                direction = animal.direction_to_move()
                if direction == 0: # we dont do anything
                    pass
                else: # we want to move, need to check what's in the position to move
                    if self._river[i+direction] == None:
                        print('move to adjesent place')
                        print('previsou state:', self._river)
                        self._river[i] = None
                        self._river[i+direction] = animal
                        print('next state:', self._river)
                    elif type(animal) == type(self._river[i+direction]):
                        type(animal)()
                        print('make_babies')
                    elif type(animal) != type(self._river[i+direction]):
                        print('bear kills fish')
                        
    

if __name__ == "__main__":
    #bear = Animal('bear')
    #print(bear.animal_type())
    #print(bear.direction_to_move())
    #fish = Animal('fish')
    #print(fish.direction_to_move())
    my_river = River(10)
    print('updating status:', my_river.update())
    #print(my_river._river[0])