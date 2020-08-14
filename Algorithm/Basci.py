def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def invert(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
    else: raise TypeError
