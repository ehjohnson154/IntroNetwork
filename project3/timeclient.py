import socket
import sys
import time

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch



website = "time.nist.gov"
port = 37

# 1. Connect to the server time.nist.gov on port 37 (the Time Protocol port).
s = socket.socket()
s.connect((website, port))

# 2. Receive data. (You don’t need to send anything.) You should get 4 bytes.

d = s.recv(4) # Receive up to 4 bytes

# 3. The 4 bytes represent a 4-byte big-endian number. Decode the 4 bytes with .from_bytes() into a numeric variable.
decoded = int.from_bytes(d, "big")

# 4. Print out the value from the time server, which should be the number of seconds since January 1, 1900 00:00.
print("NIST time: ", decoded)
# 5. Print the system time as number of seconds since January 1, 1900 00:00.
oldtime = system_seconds_since_1900()
print("Second since 1900: ", oldtime)