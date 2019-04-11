from Crypto.IO.PEM import *
from Crypto.PublicKey import RSA
from binascii import hexlify

def brute_force(c, n, e):
    for i in range(1, 1233):
        fn = "../../db/"+str(i)+".txt"
        f = open(fn, 'rb')
        for j in range(0, 769):
            f.seek(j)
            data = f.read(256)
            m = int(hexlify(data), 16)
            if pow(m, e, n) == c:
                return (i, j)

with open('pk.pem', 'rb') as fin:
    data = str(fin.read(), 'utf8')

binary, marker, decryption = decode(data)
pk = int(hexlify(binary), 16) 
ct = int(hexlify(open('ct.txt', 'rb').read()), 16)
key = RSA.import_key(binary)
ans, pos = brute_force(ct, key.n, key.e)
print('File: ', str(ans)+'.txt', 'Position: ', pos, ' to ', pos+256)
f = open('../../db/'+str(ans)+'.txt', 'r')
f.seek(pos)
data = f.read(256)
print('Data: ', data)
