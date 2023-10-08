import socket
import sys

	#pull command line arguments
website = sys.argv[1]
port = 80
#print(website)
if len(sys.argv) >= 3:
	port = sys.argv[2]

#wb = website.encode("ISO-8859-1") #encode argument?

# Ask the OS for a socket. 
s = socket.socket()

# Perform a DNS lookup to convert the human-readable name (like example.com) into an IP address 
#BYPASS THIS STEP SINCE .connect() DOES THIS FOR US

# Connect the socket to that IP address on a specific port.
#twebsite = eval(website)
#print(twebsite)
s.connect((website, port))
# Send data and receive data. This is the part we’ve been waiting for.
req = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: close \r\n\r\n".format(website)
breq = req.encode("ISO-8859-1")
s.sendall(breq)


d = s.recv(4096) # Receive up to 4096 bytes
print(d.decode())
while len(d) != 0:
	d = s.recv(4096)
	print(d.decode())

print("all done!")
s.close()



# if len(d) == 0:
# 	# all done!
# 	#s.close?
#     # Close the connection.
# 	print("all done!")
# 	s.close()