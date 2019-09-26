class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        elif type(d) == list:
            self._coords = d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        neg = Vector(len(self))
        for j in range(len(self)):
            neg[j] = -self[j]
        return neg

    def __mul__(self, nr):
        if type(nr) == int or type(nr) == float:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] *nr
        elif len(self) == len(nr):
            result = 0
            for j in range(len(self)):
                result += self[j]*nr[j]
        return result

    def __rmul__(self, nr):
        return (self * nr)


if __name__ == "__main__":
    v_one = Vector(8)
    v_two = Vector(8)
    for i in range(8):
        v_one[i] = i
        v_two[i] = i*i
    v_one[1] = 9
    v_two[1] = 7
    print(v_one, v_two)
    print(v_one - v_two)
    #print(v_one.__neg__())
    #print(-v_two)
    print('multiply:', v_one, v_one*3, 3*v_one, v_one*v_two)
    vv = Vector([1,2,3])
    v = Vector(3)
    print(vv, type(vv))
    print(v, type(v))
