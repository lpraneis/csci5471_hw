import string
import csv
'''
frequency_dict - a dict with char and overall frequency
english_text - list of all english text characters
'''
size = 1024
cipherA = bytearray(open('./cipher_aa', 'rb').read())
cipherB = bytearray(open('./cipher_ab', 'rb').read())
english_text = [' '] + list(string.ascii_uppercase) + ['\0']

xord_ciphertext = bytearray(size)
for k in range(size):
    xord_ciphertext[k] = cipherA[k] ^ cipherB[k]


with open('./ftable2.csv', mode='r') as csv_file:
    # Sets up the original frequency_dict
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    frequency_dict = dict(next(csv_reader))
    del frequency_dict['first']

    next_letter_freq ={ k:{} for k in frequency_dict.keys()}  # nested dict
    for row in csv_reader:
        rowdict = dict(row)
        for key,value in rowdict.items():
            if key == 'first':
                freq_value = value
                continue
            next_letter_freq[key][freq_value] = value
    print(next_letter_freq)

    









def translateAtoB(char, index):
    '''
    Given a position in the text and the character in A, returns what would be in B
    '''
    return str(chr(ord(char)) ^ xord_ciphertext[index])
