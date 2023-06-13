#-*- coding:utf-8 -*-
from __future__ import print_function
import string
str = "afZ_r9VYfScOeO_UL^RWUc"
num = 5
for x in str:
    i = ord(x)
    i = i + num
    print (chr(i),end='')
    num=num+1
