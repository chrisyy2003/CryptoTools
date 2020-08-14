from functools import reduce
from gmpy2 import gcd, invert as inverse


class prng_lcg:
    m = 672257317069504227  # "乘数"
    c = 7382843889490547368  # "增量"
    n = 9223372036854775783  # "模数"

    def __init__(self, seed):
        self.state = seed  # the "seed"

    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        return self.state


def solve1(N, a, b, n1):
    return (n1 - b) * inverse(a, N) % N


def solve2(N, a, n1, n2):
    b = (n2 - n1 * a) % N
    return solve1(N, a, b, n1)


def solve3(N, n1, n2, n3):
    a = (n3 - n2) * inverse(n2 - n1, N) % N
    return solve2(N, a, n1, n2)


def solve4(n1, n2, n3, n4, n5, n6):
    states = [n1, n2, n3, n4, n5, n6]
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return solve3(modulus, states[0], states[1], states[2])
