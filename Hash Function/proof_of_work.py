from pwn import *
from Crypto.Util.number import *
import re
import string
import hashlib
import random


ADDRESS = '127.0.0.1'
PORT = 10000

sh = remote(ADDRESS, 10000)


def proof_of_work():
    '''
    it will get suffix and digest from the model below
    sha256(XXXX+TsygnWMdo40yVu6J) == 8d06431e754bdd45f3a3e0375c6312d2ca52a33b79eb30f165cfda0a4b0e1a82
    it will works well if needed a little modified, 
    '''
    rec = sh.recvline().decode()
    suffix = re.findall(r'\(XXXX\+(.*?)\)', rec)[0]
    digest = re.findall(r'== (.*?)\n', rec)[0]

    print(suffix, digest)

    def f(x):
        return hashlib.sha256((x + suffix).encode()).hexdigest() == digest

    prefix = util.iters.mbruteforce(
        f, string.ascii_letters + string.digits, 4, 'fixed')
    return prefix


prefix = proof_of_work()
sh.sendlineafter('Give me XXXX:\n', prefix)

sh.interactive()
