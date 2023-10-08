import socket
s = socket.socket()

#print s

#GETS SOCKET INFORMATION

s.connect((www.example.com))

s.sendall((“Hello!”.encode())
d = s.recv()

d = s.recv(8192)
#print d
#gets massive "not implemented" text
#didn't respond in the right way, need to make a http request

#b = byte string
#\r is carriage return. think typewriter
#\n is new line
#http requires moving the character down next line, and carriage return to bring it to start of line
#get / to get "root thing" off of server
req = b"GET / HTTP/1.1\r\nHost: www.example.com\r\nConnection: close \r\n\r\n"

s.close()
s.connect((www.example.com))
s.sendall(req)


d = s.recv(8192)

#recieves massive wall of text:
#important: HTTTP/1.1 200 OK means GOOD
#servers header has bunch of metadata
#can tell when metadata ends after the "blank line"

req
#prints off

print(req.decode())
#has GET, HOST, and Connection in simple form