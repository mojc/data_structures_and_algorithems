def min_max_element(S, start):
    if start == len(S)-1:
        return S[start], S[start]
    min_el, max_el = min_max_element(S, start+1)
    return min(min_el, S[start]), max(max_el, S[start])

assert min_max_element([12, 6, 4, 7, 8, 10, 2, 0], 0) == (0, 12)
assert min_max_element([12, 6, 4, 7, 8, 10, 0, 44], 0) == (0, 44)
assert min_max_element([0, 6, 4, 7, 88, 10, 2, 4], 0) == (0, 88)

