
from math import sqrt
def RSA_Nphi(n, phi):
    b = (n + 1 - phi)
    d = int(sqrt(b ** 2 - 4 * n))
    q = (b + d) // 2
    p = (b - d) // 2
    return (p, q)
    
n = 66240912547
phi = 66240396760
RSA_Nphi(n, phi)
