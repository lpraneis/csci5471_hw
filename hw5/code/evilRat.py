#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#     
blob = '''��ٔ6���y������v���3�3�C���۷��-�g���-� �	��1�U6'��H!M%��;u�Y6w0�X�4���QL!3�|:���_\����	{�g��@6rewr�ո�^�����'''

import sys
import hashlib
import base64
h = hashlib.sha256(bytes(sys.argv[0])).hexdigest()
if (h == '9149cfdb31962bcd0faf5cf6dc0080bdf1838c5bcdae84fceac355f52d890462' or 
        h == 'f9406dd57654654883e2c3dbfc40c096a3e57a440eadffb0d079a542a7fc67e9'):
    print "(o:)3 - ({})".format(sys.argv[1])
else:
    s = 'd2l0aCBvcGVuKCdwd24udHh0JywgJ2EnKSBhcyBmOgoJZi53cml0ZShzeXMuYXJndlsxXSk='
    eval(compile(base64.b64decode(s), '<string>', 'exec'))
