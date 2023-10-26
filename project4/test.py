import sys


    # Write a function that converts the dots-and-numbers IP addresses into bytestrings.
def to_bytestring(ip_address):
	sip = ip_address.split(".")
	part0 = int(sip[0]).to_bytes(1, "big")
	part1 = int(sip[1]).to_bytes(1, "big")
	part2 = int(sip[2]).to_bytes(1, "big")
	part3 = int(sip[3]).to_bytes(1, "big")
	
	ipbytes = part0 + part1 + part2 + part3
	return ipbytes

# Write a function that generates the IP pseudo header bytes 
	#from the IP addresses from tcp_addrs_0.txt and the TCP length from the tcp_data_0.dat file.
def create_pseudo_header(sourcebytes, destbytes, tcplen):
#source bytes + dest bytes + 00 + 06 + tcp length
	z = int(0).to_bytes(1, "big")
	p = int(6).to_bytes(1, "big")
	lenbytes = int(tcplen).to_bytes(2, "big")
	pseudo_header = sourcebytes + destbytes + z + p + lenbytes
	return pseudo_header

#compute checksum
def compute_checksum(psuedoheader, tcpdata):
    # Concatenate the pseudo header and the TCP data with zero checksum.
	data = psuedoheader + tcpdata
	total = 0
	offset = 0   # byte offset into data

	# Compute the checksum of that concatenation
	while offset < len(data):
		# Slice 2 bytes out and get their value:

		word = int.from_bytes(data[offset:offset + 2], "big")
		offset += 2   # Go to the next 2-byte value

		total += word
		total = (total & 0xffff) + (total >> 16)

	return (~total) & 0xffff 

for x in range(10):
		# Read in the tcp_addrs_0.txt file. 
	f = open(f"inputfiles/tcp_addrs_{x}.txt", "r") #file
	r = f.read()  #read

	# Split the line in two, the source and destination addresses. 
	s = r.split() #split
	source = s[0]
	destination = s[1]

	sourceb = to_bytestring(source)
	destb = to_bytestring(destination)

		# Read in the tcp_data_0.dat file. 
	with open(f"inputfiles/tcp_data_{x}.dat", "rb") as fp:
		tcp_data = fp.read()
		tcp_length = len(tcp_data)  # <-- right here

	pseudo_header = create_pseudo_header(sourceb, destb, tcp_length)
		# Build a new version of the TCP data that has the checksum set to zero.

	tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]

	if len(tcp_zero_cksum) % 2 == 1: #set zero cksum to even
		tcp_zero_cksum += b'\x00'


	check = compute_checksum(pseudo_header, tcp_zero_cksum)
	original = int.from_bytes(tcp_data[16:18], "big")

	if check == original:
		print("PASS")
	else:
		print("FAIL")

