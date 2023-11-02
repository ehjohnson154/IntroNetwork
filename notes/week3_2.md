Abstracting packets of data:
variable length


Length 5
	|
+-+-+-+-+
|	|  h  e l  l  0
00 05 68 65 6C 6C 6F

00 05 h  e  l  l  o 00 03 h  i  ! 01 02  a  b  c .... #bytes, bytes and more bytes. Multiple packets
call get next packet, should only return hello packet. Next do hi. Etc etc.


gameplan:
call recv until it returns nothing
figure out length of each packet, cut that much off, continue onto next packet, repeat