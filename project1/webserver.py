import socket
import sys


port = 28333
if len(sys.argv) >= 2:
	port = sys.argv[1]



#1. Ask the OS for a socket.

s = socket.socket()

#2. Bind the socket to a port.

s.bind(('', port))

#3. Listen for incoming connections. 

s.listen()

#4. Accept incoming connections.

while True:
	print("entering server")
	new_conn = s.accept()
	new_socket = new_conn[0]  # This is what we'll recv/send on
	print("accepting connection")
	#5. Send data and receive data. 
	#note; "\r\n\r\n" is when you've read enough

	stuff = new_socket.recv(4096).decode()
	while "\r\n\r\n" not in stuff:
		stuff = new_socket.recv(4096).decode()
	print("accepted data")

	response = "HTTP/1.1\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!"
	bresponse= response.encode("ISO-8859-1")
	new_socket.sendall(bresponse)
	#Simple response should be:
	# HTTP/1.1 200 OK
	# Content-Type: text/plain
	# Content-Length: 5
	# Connection: close

	# Hello!
	#"HTTP/1.1\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\n Hello!"

	#6. Go back and accept another connection.
	print("closing connection")
	new_socket.close()

	#loop back to s.accept()