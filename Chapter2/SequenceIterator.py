class SequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        return self

class ReversedSequenceIterator(SequenceIterator):
    def __init__(self, sequence):
        super().__init__(sequence)
        self._k = len(self._seq)
    
    def __next__(self):
        self._k -= 1
        if self._k >= 0:
            return (self._seq[self._k])
        else:
            raise StopIteration()
    def __iter__(self):
        return self

print([x for x in ReversedSequenceIterator([1,2,3,4,5, 6, 7, 8])])