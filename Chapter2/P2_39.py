from abc import abstractmethod


class Polygon():
    def __init__(self, nr_edges, len_edges):
        self._nr_edges = nr_edges
        self._len_edges = len_edges
        assert self._nr_edges == len(len_edges)

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Triangle(Polygon):
    def perimeter(self):
        super().perimeter()
        return sum(self._len_edges)

    def area(self):
        super().area()
        p = self.perimeter()
        return round((p * (p - self._len_edges[0]) * (p - self._len_edges[1]) + (
            p - self._len_edges[2])) ** (1/2), 2)


if __name__ == "__main__":
    t = Triangle(3, [2, 3, 4])
    print(t.perimeter(), t.area())
