from Progression import Progression


class AbsDiffProgression(Progression):
    def __init__(self, first=2, second=200):
        self._previous = first
        self._current = second

    def _advance(self):
        self._tmp = abs(self._previous - self._current)
        self._previous = self._current
        self._current = self._tmp
        return self._tmp


if __name__ == "__main__":
    abs_prog = AbsDiffProgression()
    abs_prog.print_progression(8)
    abs_prog = AbsDiffProgression(5, 9)
    abs_prog.print_progression(8)
    abs_prog = AbsDiffProgression(-100, 2)
    abs_prog.print_progression(8)
