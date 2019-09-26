import itertools
letters = ['c', 'a', 't', 'd', 'o', 'g']
options = list(itertools.permutations(letters))
result = [''.join(option) for option in options]
print(result)