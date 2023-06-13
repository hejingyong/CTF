#——*coding:utf-8*-
 
def VigenereEncryto(min,key):
	MinLen=len(min)#明文长度
	KeyLen=len(key)#密钥长度
	(q,r)=divmod(MinLen,KeyLen)#q商 r余数
	out=""
	#完整映射密钥的加密
	for i in range(0,q):
		for j in range(0,KeyLen):
		#谈谈核心代码理解结合实例
		#密钥:R
		#明文:T
		#密文:K：
		#(R-A)%26+A和（T-A）%26+A得到K===>（T-A+R-A）%26+A
		#（T-A）%26+A就是以A开头第T个元素，A与R列对齐意思即是，(R-A)%26+A就是以R头字母表，R之后的第T-A元素
			c=int((ord(min[i*KeyLen+j])-ord('A')+ord(key[j])-ord('A'))%26+ord('A'))
			out+=chr(c)
	#残余映射密钥加密
	for i in range(0,r):
		c=int((ord(min[q*KeyLen+i])-ord('A')+ord(key[i])-ord('A'))%26+ord('A'))
		out+=chr(c)
	return out
	
def VigenereDecryto(anwen,key):
	AnLen=len(anwen)#明文长度
	KeyLen=len(key)#密钥长度
	(q,r)=divmod(AnLen,KeyLen)#q商 r余数
	out=""
	#完整映射密钥的加密
	for i in range(0,q):
		for j in range(0,KeyLen):
		#已知暗文位置减去A,加上Z减去key的位置就是，A到明文长度
		#K-A+1   + Z-R===〉T-A
			c=int((ord(anwen[i*KeyLen+j])-ord('A')+1+ord('Z')-ord(key[j]))%26+ord('A'))
			out+=chr(c)
	#残余映射密钥加密
	for i in range(0,r):
		c=int((ord(anwen[q*KeyLen+i])-ord('A')+1+ord('Z')-ord(key[i]))%26+ord('A'))
		out+=chr(c)
	return out
def Lower(str):
	u=""
	for i in str:
		u+=i.lower()
	return u
 
if __name__=='__main__':
	num=input('选择维吉尼亚模式：1加密，2解密： ')
	if(num=='1'):
		str=input('请输入明文： ')
		key=input('请输入密钥： ')
		print('加密后的密文： '+VigenereEncryto(str,key))
		print('密文转化成小写： '+Lower(VigenereEncryto(str,key)))
	elif(num=='2'):
		str=input('请输入密文： ')
		key=input('请输入密钥： ')
		print('解密后的明文： '+VigenereDecryto(str,key))
		print('明文转化成小写： '+Lower(VigenereDecryto(str,key)))
	else:
		print('Error')
