def cout_vowels(seq):
    seq = seq.lower()
    return sum([letter in ['a', 'e', 'i', 'o', 'u'] for letter in seq])

print(cout_vowels('abcbeboU'))