from hashlib import sha256
from binascii import hexlify
import io


def modinv(a, m):
    a = a % m
    if a < 0:
        x, y = egcd(-a, m)
    else:
        x, y = egcd(a, m)
    return x % m

def egcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b,  a%b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def decode(filename):
    with open(filename, 'rb') as fin:
        data = io.BytesIO(fin.read())
    if data.read(1) != b'\x02':
        print('Not integer!')
        return None
    val = data.getvalue()
    integer = val[3:]
    return int(hexlify(integer), 16)

p_val = decode('p.txt')
q_val = decode('q.txt')

n = p_val * q_val
e = int(sha256(b'prane001').hexdigest(), 16)
d = modinv(e, n)

print('n', n)
print('e', e)
print('d', d)
print('check', (e * d) % n)
