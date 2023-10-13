import os
import socket
import sys


# PROJECT 2
# We’re going to make it so that when a web client 
# (in this case we’ll use a browser) 
# requests a specific file, the webserver will return that file.

##STEPS:##

# Parse that request header to get the file name.
# Strip the path off for security reasons.
def get_filename(header): #returns filename (ex: file1.txt)

    parsedget = header.split("\r\n")
    parsedfilename = os.path.split(parsedget[0])
    prefilename = parsedfilename[0]
    preprefilename = prefilename.split()
    pppfilename = preprefilename[1]
    #print(pppfilename)
    stuff= os.path.split(pppfilename)
    #print(stuff)
    filename = stuff[1]

    #print(header)
    print("-----------------")
    print("filename is ", filename)
    return filename

# Determine the type of data in the file, HTML or text.
def get_filetype(filename):
    
    prefiletype = os.path.splitext(filename)
    filetype = prefiletype[1]
    print("filetype is ", filetype)
    if filetype == ".txt":
         return "text/plain"
    if filetype == ".html":
        return "text/html"
    if filetype == ".gif":
        return "image/gif"
    else:
        print("error filetype")
        return filetype
	
def read_data(filename): #returns data, or 404

        # Read the data from the named file.
    try:
        with open(filename, "rb") as fp:
            data = fp.read()   # Read entire file
            print("checking data")
            print(data[:5])
            return data

    except Exception as x:
        
        # File not found or other error
        print("404")
        print(filename)
        print(x)
        
        return "404 not found"

# Build an HTTP response packet with the file data in the payload.
def prepare_package(data, filetype):

    #bdata = data.encode("ISO-8859-1")
    length = len(data)
    response = "HTTP/1.1\r\nContent-Type: {}\r\nContent-Length: {}\r\nConnection: close\r\n\r\n".format(filetype, length)
    bresponse = response.encode("ISO-8859-1")
    bresponse += data
    return bresponse

#print("test")
# Send that HTTP response back to the client. IN SERVER

#########################

port = 28333
if len(sys.argv) >= 2:
	port = sys.argv[1]

#1. Ask the OS for a socket.

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
    print("preparing to read request")
    filename = get_filename(stuff)
    filetype = get_filetype(filename)
    data = read_data(filename)
    response = prepare_package(data, filetype)
    print("prepared package")

    # response = "HTTP/1.1\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!"
    # bresponse= response.encode("ISO-8859-1")
    new_socket.sendall(response)
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