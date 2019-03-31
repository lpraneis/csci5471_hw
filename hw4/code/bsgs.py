from math import ceil, sqrt
from hashlib import sha256

def bsgs(base, n, prime):
    N = ceil(sqrt(prime -1))
    powDict = {}
    for i in range(N):
        powDict[ pow(base, i, prime)] = i

    c = pow(base, N * (prime-2), prime)

    for j in range(N):
        y = (n * pow(c, j, prime)) % prime
        if y in powDict:
            return j * N + powDict[y]
    return None

n = int(sha256(b'prane001').hexdigest(), 16)
prime = 922736209
print(bsgs(7, n, prime ))

