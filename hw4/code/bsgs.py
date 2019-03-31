from math import ceil, sqrt
from hashlib import sha256

n = int(sha256(b'prane001').hexdigest(), 16)

def bsgs(base, n, prime):
    N = ceil(sqrt(prime -1))

    tbl = {pow(base, i, prime): i for i in range(N)}

    c = pow(base, N * (prime-2), prime)

    for j in range(N):
        y = (n * pow(c, j, prime)) % prime
        if y in tbl:
            return j * N + tbl[y]
    return None

prime = 922736209
print(bsgs(7, n, prime ))

