

# This week's project: Improve the web server
# Group work: design some functions
# Discussion: Internet Protocol

# IPv4
# IPv6

# GET /favicon.ico HTTP/1.1
# GET /Keyboardcat.gif HTTP/1.1

# #think of how we type stuff in the web
# http://example.com/keyboardcat.gif

# MIME Type:
# *text/html
# *text/plain
# *ect etc...

# response:

# HTTP/1.1 200 ok
# Content-Type: Text/html


# ###########
# GET /../../../../../../../etc/passwrd HTTP/1.
# ##########

# Steps:

# 1. EXtract path and file from GET line
# 2. Split extension off
# 3. Map extension to mime type
# 4. FInd the file
# 5. Read in the file data
# 6. Get the length of the data 
# 7. Serve it back to the client 

# #Will never get:
# GET /my 20image.gif HTTP/1.1
# #will always be encoded into:
# GET /my%20image.gif HTTP/1.1