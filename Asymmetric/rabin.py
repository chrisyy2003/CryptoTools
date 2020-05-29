from Crypto.Util.number import *
from Algorithm import tonelli_shanks
from libnum import solve_crt

def Rabin(p, q, c):
    t = tonelli_shanks(c, p)
    qlist = [-t, t]
    t = tonelli_shanks(c, q)
    plist = [-t, t]
    for i in qlist:
        for j in plist:
            print(long_to_bytes(solve_crt([i, j], [p, q])))


p = getPrime(512)
q = getPrime(512)
e = 2
n = p * q
m = b'flag{this_is_flag}'
c = pow(bytes_to_long(m), e, n)

Rabin(p, q, c)



