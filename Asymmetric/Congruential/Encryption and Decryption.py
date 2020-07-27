from Crypto.Util.number import * 
from gmpy2 import iroot


def Encryption(m):
    while True:
        q = getPrime(1024)
        f = getPrime(512)
        g = getPrime(512)
        if f < iroot(q // 2, 2)[0] and iroot(q // 4, 2)[0] < g and g < iroot(q // 2, 2)[0] and GCD(f, q) == 1:
            break

    h = (inverse(f, q) * g) % q
    m = bytes_to_long(m)
    r = getPrime(510)
    assert (0 < m and m < iroot(q // 4, 2)[0])
    assert (0 < r and r < iroot(q // 2, 2)[0])
    e = (r * h + m) % q
    return (f, g, q, h, e)

def Decryption(f, g, e, q):
    a = f * e % q
    m = inverse(f, g) * a % g
    print(long_to_bytes(m))


f, g, q, h, e = Encryption(b'flag{this_is_flag}')
print(e)
print(q)
print(h)
Decryption(f, g, e, q)
