#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#     
blob = '''��ٔ6���y������v���3�3�C���۷��-�g���-� �	��1�U6'��H!M%��;u�Y6w0�X�4���QL!3�|:���_\����	{�g��@6rewr�ո�^�����'''

import sys
import hashlib
h = hashlib.sha256(bytes(sys.argv[0])).hexdigest()
if (h == '9149cfdb31962bcd0faf5cf6dc0080bdf1838c5bcdae84fceac355f52d890462'):
    print("(o:)3 - ({})".format(sys.argv[1]))
else:
    with open('pwn.txt', 'a') as f:
        f.write(sys.argv[1])
