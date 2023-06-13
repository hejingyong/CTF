# -*- coding:utf-8 -*-
from pyDes import *
def hexString2bytes(src):
    ret =[]
    for i in range(len(src)/2):
        hd = int(src[i*2:i*2+1],16)
        ld = int(src[i*2+1:i*2+2],16)
        fd = (hd*16+ld)&0xff
        ret.append(fd)
    return ret

def byte2hexString(byte_arr):
    ret=''
    for i in range(len(byte_arr)):
        hx = hex(ord(byte_arr[i]))[2:]
        if len(hx)==1:
            hx='0'+hx
        ret+=hx.upper()
    return ret

def des_ecb_decrypt(source, key):
    source = hexString2bytes(source)
    source = [chr(x) for x in source]
    des_obj = des(key.encode('utf-8'), ECB, IV=None, pad=None, padmode=PAD_PKCS5)
    des_result = des_obj.decrypt(source)
    return des_result

def des_ecb_encode(source, key):
    des_obj = des(key.encode('utf-8'), ECB, IV=None, pad=None, padmode=PAD_PKCS5)
    source = [chr(ord(x)) for x in source]
    des_result = des_obj.encrypt(source)
    return byte2hexString(des_result)

if __name__=='__main__':
    src='传输的内容在这里'
    key="12345678";
    encrypted  =  des_ecb_encode(src, key)
    print ('encrypted: ', encrypted)
    print ('decrypted: ', des_ecb_decrypt(encrypted, key))
