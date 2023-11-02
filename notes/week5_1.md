


& Bitwise AND
| Bitwise OR
~ Bitwise NOT
^ Bitwise Exclusive-OR

//////

	10011001
&	10111010
-----------------
	10011000


	|	Network Number			  |Host|
	10011001.01001010.11010110.11 011110

Network Number:
	10011001.01001010.11010110.11 000000

Host:
	0000000.00000000.00000000.00 011110

Sliding scale between network and subnets

Subnet Mask: (Same as '/26'):
	11111111.11111111.11111111.11 000000

	-26 bits that are 1
	-Gives us all the information we need to split network number from host number

	10011001.01001010.11010110.11 011110 IP
&	11111111.11111111.11111111.11 000000 Mask
	--------------------------------------
	10011001.01001010.11010110.11 000000 Network #

192.168.0.2/24

##Subnet and Subnet mask##

Entire Internet:
	0000000.00000000.00000000.00000000

Subnet by adding subnet bits
	1100000.00000000.00000000.00000000

Example:
We're networ;
	0100000.00000000.00000000.00000000/2
	01 001
	01 010
	01 011
	01 100
	01 101
	01 110
	01 111
Megacorp splitting up into 8 other mega networks, which can be solt by those companies into further subnets...




