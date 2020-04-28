from Crypto.Util.number import long_to_bytes
import libnum

p = 1
q = 1
c = ''
b1 = pow(c, (p + 1) // 4, p)
b2 = pow(c, (q + 1) // 4, q)
ans = []
ans.append(libnum.solve_crt([b1, b2], [p, q]))
ans.append(libnum.solve_crt([-b1, b2], [p, q]))
ans.append(libnum.solve_crt([b1, -b2], [p, q]))
ans.append(libnum.solve_crt([-b1, -b2], [p, q]))
for i in ans:
    print(long_to_bytes(i))
