from collections import Counter
import matplotlib.pyplot as plt


class LetterHistogram():
    def __init__(self, path):
        self._path = path
        self._data = self._read_doc()

    def _read_doc(self):
        with open(self._path, 'r') as f:
            data = f.read().replace('\n', '').lower()
        return data

    def cnt_letters(self):
        txt = [letter for letter in self._data if letter.isalpha()]
        cnt = Counter(txt)
        return cnt
    
    def plot_hist(self):
        cnt = self.cnt_letters()
        plt.bar(cnt.keys(), cnt.values())
        plt.show()


LetterHistogram('Chapter2/test_txt.txt').plot_hist()
