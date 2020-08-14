def egcd(a, b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q, r = divmod(a, b)
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, r
    return u, v, a


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def LineCongSolver(a, c, m):
    g = gcd(a, m)
    if c % g:
        return None
    u0 = egcd(a, m)[0]
    return [(c * u0 + k * m) // g % m for k in range(g)]


def CRT(ai, mi):
    assert(isinstance(mi, list) and isinstance(ai, list))
    a_s, m = set([ai[0]]), mi[0]
    for a1, m1 in zip(ai[1:], mi[1:]):
        new_as = set()
        for a in a_s:
            ks = LineCongSolver(m, a1 - a, m1)
            if not ks:
                continue
            for k in ks:
                new_as.add(a + k*m)
        a_s = new_as
        m = m * m1
    return a_s, m

if __name__ == '__main__':
    import hashlib

    ms = [284461942441737992421992210219060544764, 218436209063777179204189567410606431578, 288673438109933649911276214358963643204, 239232622368515797881077917549177081575,
          206264514127207567149705234795160750411, 338915547568169045185589241329271490503, 246545359356590592172327146579550739141, 219686182542160835171493232381209438048]
    cs = [273520784183505348818648859874365852523, 128223029008039086716133583343107528289, 5111091025406771271167772696866083419, 33462335595116820423587878784664448439,
          145377705960376589843356778052388633917, 128158421725856807614557926615949143594, 230664008267846531848877293149791626711, 94549019966480959688919233343793910003]

    sol = CRT(cs, ms)
    for x in sol[0]:
        if "4b93deeb" in hashlib.sha256(str(x).encode()).hexdigest():
            flag = "flag{" + hashlib.sha256(str(x).encode()).hexdigest() + "}"
            print(flag)
            break


