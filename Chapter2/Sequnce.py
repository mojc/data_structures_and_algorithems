from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):

    @abstractmethod
    def __getitem__(self, j):

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for j in range(len(self)):
                if self[j] != other[j]:
                    return False
            return True

    def __lt__(self, other):
        for j in range(min(len(self), len(other))):
            if self[j] != other[j]: 
                return False
        return True