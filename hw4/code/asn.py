import asn1
from hashlib import sha256

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

p_bytes = open('p.txt', 'rb').read()
q_bytes = open('q.txt', 'rb').read()

decoder = asn1.Decoder()
decoder.start(p_bytes)
tag, p_val = decoder.read()
decoder.start(q_bytes)
tag, q_val = decoder.read()

n = p_val * q_val
e = int(sha256(b'prane001').hexdigest(), 16)
d = modinv(e, n)

print('n', n)
print('e', e)
print('d', d)
print('check', (e * d) % n)




