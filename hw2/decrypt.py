import subprocess
byte_i = bytearray(b'0'*8)

def shift_left(ct_index):
    for i in range(1, len(byte_i)):
        byte_i[i-1] = byte_i[i]

def guess_pos(ct_index):
    iv = get_iv() #setting the IV
    zero_block = bytearray(b'0' * ct_index) 
    encrypyted = encrypt(bytearray(iv)+zero_block) # should fill in missing place with ciphertext spot 1
    test_byte = byte_i
    target = encrypyted[16:24] # this is ek2 of the secret string. Need to match that!
    for byte in range(0, 256):
        first_block = get_iv()
        test_byte[7] = byte
        test_enc = encrypt(first_block + bytearray(test_byte))
        if (test_enc[16:24] == target):
            byte_i[7] = byte
            break

path_to_next_iv = '/class/csci5471/hw2/nextIV'
# get_iv : unit -> bytearray
def get_iv():
    with subprocess.Popen(path_to_next_iv,stdout=subprocess.PIPE,stdin=subprocess.DEVNULL) as niv:
        iv = niv.stdout.read(8)
    return iv

path_to_buffer = '/class/csci5471/hw2/buffer'
path_to_encrypt = '/class/csci5471/hw2/encrypt'
# encrypt : bytearray -> bytearray
def encrypt(s):
    with subprocess.Popen(path_to_buffer,stdin=subprocess.PIPE,stdout=subprocess.DEVNULL) as buf:
        buf.stdin.write(s)
    with subprocess.Popen(path_to_encrypt,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE) as enc:
        ctxt = enc.stdout.read()
    return ctxt

for i in range(7,-1, -1):
    guess_pos(i)
    if i != 0:
        shift_left(i)
print(byte_i)
