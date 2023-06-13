
#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
alphabet=['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 
one_biao=["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab",
"aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa",
"abbab","abbba","abbbb","baaaa","baaab","baaba","baabb",
"babaa","babab","babba","babbb","bbaaa","bbaab"]
 
def encode():
#python3.0版本后用input替换了raw_input
	string=input('请输入字符串加密')#明文
	e_string=""
	for index in string:
		for i in range(0,26):
			if(index==alphabet[i]):#字母匹配
				e_string+=one_biao
				break
	print('编码'+e_string)
	return
	
def decode():
	e_string=input('请输入暗文解密')
	e_array=re.findall(".{5}",e_string)
	d_string=""
	for index in e_array:
		for i in range(0,26):
			if index==one_biao[i]:
				d_string+=alphabet[i]
	print("解码为："+d_string)
	return
 
if __name__=="__main__":
	number=input('输入数1或2，1加密，2解密: ')
	if number=="1":
		encode()
	elif number=='2':
		decode()


#原文链接：https://blog.csdn.net/dongyanwen6036/article/details/76404098
