

Encoding of data

Of integers, specifically
Endianess
Group exercise: convert a bunch of numbers

Project 3:


Encoding of data
0b1000000010 binary (base 2) decimal 258

00000001 00000010
	1		2
	01		02

11111111 11111111
	255		255
	FF		FF


2789364
4e e8 a2
2a 8f f4
10000
131071
128 -> 0b10000000 (binary) -> 0x80 (hexidecimal) -> 16 (bytes)

Python has method called .to_bytes(4) (can put variable instead of number)

\x means hexadecimal byte string