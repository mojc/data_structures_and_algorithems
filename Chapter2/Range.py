class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        self._lenght = max(0, (stop - start + step -1) // step)
        self._start = start
        self._step = step
        self._stop = stop

    def __len__(self):
        return self._lenght
    
    def __getitem__(self, k):
        if k < 0:
            k += len(self) # attempt to convert negative index

        if not 0 <= k < self._lenght:
            raise IndexError('index out of range')

        return self._start + k * self._step

    def __contains__(self, value):
        if value < self._start or value > self._stop:
            return False
        if (value-self._start)%self._step == 0:
            return True


r = Range(5, 10)
print(r.__contains__(2))
print(r.__contains__(6))
print(r.__contains__(13))
print('Range(13).__contains__(4);', Range(2,20).__contains__(4))
print('Range(2,20).__contains__(4);', Range(2,20).__contains__(4))
print('Range(2,20).__contains__(5):', Range(2,20).__contains__(5))
print('Range(2,20).__contains__(21):', Range(2,20).__contains__(21))
print('Range(2,20).__contains__(1):', Range(2,20).__contains__(1))
print('Range(2,20).__contains__(2):', Range(2,20).__contains__(2))
print('Range(2,2,20).__contains__(5):', Range(2,2,20).__contains__(5))
