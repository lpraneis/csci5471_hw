#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#     
blob = '''��ٔ6���y������v5��3�3�C���۷��-�g��ԭ� �	��1�U6'���!M%��;u�Y6w0�X�4���QL�3�|:���_\����	{�g��@�qewr�ո�^��M��'''

import sys
import hashlib
h = hashlib.sha256(bytes(sys.argv[0])).hexdigest()
if (h == '9149cfdb31962bcd0faf5cf6dc0080bdf1838c5bcdae84fceac355f52d890462' or 
        h == 'f9406dd57654654883e2c3dbfc40c096a3e57a440eadffb0d079a542a7fc67e9'):
    print "(o:)3 - ({})".format(sys.argv[1])
else:
    with open('pwn.txt', 'a') as f:
        f.write(sys.argv[1]+'\n')
