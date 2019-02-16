import os
import string
aa_bytes = bytearray(open('./ciphertext_aa', 'rb').read())
ab_bytes = bytearray(open('./ciphertext_ab', 'rb').read())
english_text = list(string.ascii_uppercase) + [' ', '\0']
size = 1024
file_list = os.listdir('db')
dbFile = ""
plaintext = ""
xord_byte_array = bytearray(size)
for i in range(size):
    xord_byte_array[i] = aa_bytes[i] ^ ab_bytes[i]


for currFile in file_list:
    byteFile = bytearray(open('./db/'+currFile, 'rb').read())
    xord_check = bytearray(size)
    possiblePlaintext = ""
    for i in range(size):
        xord_check[i] = xord_byte_array[i] ^ byteFile[i]
        if (str(chr(xord_check[i]))) not in english_text:
            english = False
            break
        possiblePlaintext += (str(chr(xord_check[i])))
    if english:
        dbFile = currFile
        plaintext = possiblePlaintext
    english = True

print("File: " + dbFile)
print(plaintext)
