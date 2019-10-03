import math
from Progression import Progression


class SqRootProgression(Progression):
    def __init__(self, start=65536):
        self._current = start

    def _advance(self):
        self._current = math.sqrt(self._current)
        return self._current


if __name__ == "__main__":
    SqRootProgression().print_progression(10)
