# -*- coding:utf-8 -*-

import hashlib

def passEncrypt(password):
    module = hashlib.md5()
    passByte = password.encode(encoding='utf-8', errors = 'strict')
    module.update(passByte)
    encryptPass = module.hexdigest()

    return encryptPass
