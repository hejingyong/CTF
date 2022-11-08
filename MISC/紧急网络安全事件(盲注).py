import urllib.parse
import requests,re
preTime = None
preKey = None
preValue = None
f = open('紧急网络安全事件(盲注).log','r',encoding='gb18030',errors='ignore')
lines = f.readlines()
flag_ascii = {}
for line in lines:
    if len(line) > 2:
        request = urllib.parse.unquote(urllib.parse.unquote(line))

        # (LIMIT 0,1\),(.*?),1\)\)!=(.*?),0,1\)
        matchObj = re.search(r'\[(.*?) -0500.*limit 0,1\),(.*?),1\)=binary\(\'(.*?)\'\),1,sleep\(3\)',request)
        if matchObj:
            curTime  = matchObj.group(1)
            if preTime == curTime:
                #key = int(matchObj.group(2))  
                #value = ord(matchObj.group(3))  
                flag_ascii[preKey] = preValue
            # print(matchObj.group(2),':',matchObj.group(3))
            preTime = curTime
            preKey = int(matchObj.group(2)) 
            preValue = ord(matchObj.group(3))        
flag = ''
for value in flag_ascii.values():
    flag += chr(value)
print (flag)

