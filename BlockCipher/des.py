from functools import reduce
import numpy as np
from Crypto.Util.number import long_to_bytes

# 整数转二进制数组，指定位长 n，大端序


def int2bin(a, n):
    assert 0 <= n and a < 2**n
    res = np.zeros(n, dtype=int)

    for x in range(n):
        res[n-x-1] = a % 2
        a = a // 2
    return res.tolist()

# 二进制数组转整数，大端序
def bin2int(a):
    return reduce(lambda x, y: x * 2 + y, a)

def bin2bytes(a):
    a = np.array(a, dtype=int).reshape(8, 8)
    res = ''
    for i in range(8):
        res += hex(bin2int(a[i]))[2:]
    return bytes.fromhex(res)

# 循环左移off位
def leftRotate(a, off):
    return a[off:] + a[:off]


# 块异或
def BlockXor(a, b):
    assert len(a) == len(b)
    return [x ^ y for x, y in zip(a, b)]


# 选择置换1
# 从64位输入密钥中选择56位，分为左右两个28位半密钥
def PC1(key):
    pc1_l = [57, 49, 41, 33, 25, 17, 9,
             1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27,
             19, 11, 3, 60, 52, 44, 36]
    pc1_r = [63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 28, 20, 12, 4]

    return [key[x - 1] for x in pc1_l], [key[x - 1] for x in pc1_r]

# 选择置换2
# 从56位的密钥中选取48位子密钥


def PC2(key):
    assert len(key) == 56

    pc2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]
    return [key[x - 1] for x in pc2]

# 子密钥生成算法，由一个64位主密钥导出16个48位子密钥


def keyGen(key):
    assert len(key) == 64

    l, r = PC1(key)
    off = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    res = []
    for x in range(16):
        l = leftRotate(l, off[x])
        r = leftRotate(r, off[x])

        res.append(PC2(l + r))

    return res

# 初始置换


def IP(a):
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    return [a[x-1] for x in ip]


# Feistel网络:S盒变换，输入48位，输出32位
def S(a):
    assert len(a) == 48

    S_box = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
              0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
              4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
              15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
             [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
                 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
                 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
              13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
             [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
                 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
                 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
                 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
             [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
                 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
                 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
                 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
             [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
                 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
                 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
                 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
             [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
                 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
                 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
                 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
             [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
                 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
                 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
                 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
             [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
                 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
                 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
                 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    a = np.array(a, dtype=int).reshape(8, 6)
    res = []
    for i in range(8):
        # 用 S_box[i] 处理6位a[i]，得到4位输出
        p = a[i]
        r = S_box[i][bin2int([p[0], p[5], p[1], p[2], p[3], p[4]])]
        res.append(int2bin(r, 4))

    res = np.array(res).flatten().tolist()
    assert len(res) == 32

    return res

# Feistel网络: 扩展置换，将32位的半块扩展到48位


def Expand(a):
    assert len(a) == 32
    e = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    return [a[x - 1] for x in e]

# Feistel网络:P置换


def P(a):
    assert len(a) == 32

    p = [16, 7, 20, 21,
         29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2, 8, 24, 14,
         32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25]
    return [a[x - 1] for x in p]


# F函数，用于处理一个半块
def Feistel(a, subKey):
    assert len(a) == 32
    assert len(subKey) == 48

    eHalfBlock = BlockXor(Expand(a), subKey)
    xHalfBlock = S(eHalfBlock)
    sHalfBlock = P(xHalfBlock)

    return sHalfBlock


# 最终置换
def FP(a):
    fp = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]
    return [a[x-1] for x in fp]


def DES_enc(m, key):

    if type(m) != bytes:
        raise TypeError("message must be type `bytes`")
    elif len(m) != 8:
        raise ValueError("message must be 64-bit in length")
    if type(key) != bytes:
        raise TypeError("key must be type `bytes`")
    elif len(key) != 8:
        raise TypeError("key must be 64-bit in length`")
    subkey = int(key.hex(), 16)
    m = int(m.hex(), 16)

    subkeys = keyGen(int2bin(subkey, 64))  # 16轮子密钥生成

    m = IP(int2bin(m, 64))  # 初始置换
    l, r = np.array(m, dtype=int).reshape(2, -1).tolist()
    for i in range(16):
        l, r = r, BlockXor(l, Feistel(r, subkeys[i]))  # 16轮轮函数
    c = FP(r + l)  # 最终置换

    return long_to_bytes(bin2int(c))  # 块转10进制转字节

def DES_dec(m, key):
    subkey = int(key.hex(), 16)
    m = int(m.hex(), 16)

    subkeys = keyGen(int2bin(subkey, 64))  # 16轮子密钥生成
    subkeys = subkeys[::-1]

    m = IP(int2bin(m, 64))  # 初始置换
    l, r = np.array(m, dtype=int).reshape(2, -1).tolist()
    for i in range(16):
        l, r = r, BlockXor(l, Feistel(r, subkeys[i]))  # 16轮轮函数
    c = FP(r + l)  # 最终置换

    return long_to_bytes(bin2int(c))  # 块转10进制转字节

if __name__ == "__main__":
    print(DES_dec(DES_enc(b'chrisyyy', b'12345678'), b'12345678'))



