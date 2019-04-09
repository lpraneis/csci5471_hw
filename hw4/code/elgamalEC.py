from sys import argv
from random import randrange, getrandbits

def is_prime(n):
    if n ==2 or n ==3: 
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s =0
    r = n-1
    while r&1 == 0:
        s+=1
        r //=2
    for _ in range(32): # 32 tests of Miller Rabin
        a = randrange(2, n-1)
        x = pow(a, r, n)
        if x != 1 and x != n-1:
            j = 1
            while j < s and x != n-1:
                x = pow(x, 2, n)
                if x ==1:
                    return False
                j += 1
            if x != n -1:
                return False
    return True

def generate_candidate(length):
    p = getrandbits(length)
    p |= ( 1<< length -1) | 1
    return p

def generate_prime(length):
    p = 4
    while not is_prime(p):
        p = generate_candidate(length)
    return p


def gcd(a, b):
    q, r = 0,0
    while(b > 0):
        q = a/b
        r = a - q*b
        a = b
        b = r
    return a

def find_generator(p):
    for i in range(2, p):
        print(i)
        if gcd(i, p-1) == 1:
            return i

def add():
    keyfile = argv[2]
    cfile1 = argv[3]
    cfile2 = argv[4]
    outfile = argv[5]

def decrypt():
    keyfile = argv[2]
    ctextfile = argv[3]

def genkey():
    nbits = argv[2]
    pubfile = argv[3]
    privfile = argv[4]
    sk = open(privfile, 'wb')
    pk = open(pubfile, 'wb')

    p = generate_prime(1024)
    

def encrypt():
    keyfile = argv[2]
    msg = argv[3]
    ctextfile = argv[4]


if argv[1] == 'genkey':
    genkey()
elif argv[1] == 'encrypt':
    encrypt()
elif argv[1] == 'decrypt':
    decrypt()
elif argv[1] == 'add':
    add()
