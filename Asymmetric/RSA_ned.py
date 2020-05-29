from gmpy2 import next_prime, gcd
from Crypto.Util.number import *
def RsaNed(n, e, d):
    g = 2
    while True:
        k = e * d - 1
        while not k & 1:
            k //= 2
            p = int(gcd(pow(g, k, n) - 1, n)) % n
            if p > 1:
                return p
        g = next_prime(g)

p = getPrime(512)
q = getPrime(512)
n = q * p
e = 0x10001
d = inverse(e, (p - 1) * (q - 1))
print(p)
print(RsaNed(n, e, d))
