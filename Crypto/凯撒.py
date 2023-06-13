#实现大小写字母并行平移
def change1(c,i):
	num=ord(c)
	if(num>=97 and num<=122):  
		num=97+(num+i-97)%(26)  
	return chr(num)
def change2(c,i):
	num=ord(c)
	if(num>=65 and num<=90):  
		num=65+(num+i-65)%(26)  
	return chr(num)	
 
      
def kaisa_jiAmi(string,i):  
	string_new=''  
	for s in string:
		num=ord(s)
		if(num>=97 and num<=122 ):
			string_new+=change1(s,i)
		elif(num>=65 and num<=90 ):
			string_new+=change2(s,i)
	print(string_new)  
	return string_new  
  
#本题有种暴力解密感觉  
def kaisa_jiEmi(string):  
	for i in range(0,26):  
		print('第'+str(i+1)+'种可能:',end='   ')  
		#区别在于 string 是该对象原本就是字符串类型, 而 str()则是将该对象转换成字符串类型。  
		kaisa_jiAmi(string,i)  
          
#你要知道input输入的数据类型都是string     
def main():  
	print('请输入操作，注意默认小写，大写同理:')  
	choice=input('1:恺撒加密,2:凯撒穷举解密.请输入1或2：')  
	if choice=='1':  
		string=input('请输入需要加密字符串： ')  
		num=int(input('请输入需要加密的KEY： '))  
		kaisa_jiAmi(string,num)  
	elif choice=='2':  
		string=input('请输入需要解密字符串： ')  
		kaisa_jiEmi(string)  
	else:  
		print('输入错误，请重试')  
		main()  
          
if __name__=='__main__':  
	main()  
#原文链接：https://blog.csdn.net/dongyanwen6036/article/details/76716373
