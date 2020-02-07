# R_41
def max_element(S, start):
    if start == len(S)-1:
        return S[start]
    return max(S[start], max_element(S, start+1))

assert max_element([12, 6, 4, 7, 8, 10, 2, 4], 0) == 12
assert max_element([12, 6, 4, 7, 8, 10, 2, 44], 0) == 44
assert max_element([12, 6, 4, 7, 88, 10, 2, 4], 0) == 88

# Running time O(n), space usage O(n)

# R_42
# power(2, 5)  -> 16*2=32
# 2**4  -> 8*2=16
# 2**3  -> 4*2=8
# 2**2  -> 2*2=4
# 2**1  -> 2*1=2
# 2**0  -> 1

# R_43
# power(2, 18)    ->  512*512 = 262144
# power(2, 9)     ->  16*16*2 = 512
# power(2, 4)     ->  4*4 = 16
# power(2, 2)     ->  2*2 = 4
# power(2, 1)     ->  1*1*2 = 2
# power(2, 0)     ->  1

# R_46
def harmonic_number(n):
    if n == 0:
        return 0
    return 1 / n + harmonic_number(n-1)

assert harmonic_number(0) == 0
assert harmonic_number(1) == 1
assert harmonic_number(2) == 1.5
assert round(harmonic_number(10), 3) == 2.929

# R_48
# O(n) -> half the sequence each time; sum(n/2**1), i=1 to inf = n