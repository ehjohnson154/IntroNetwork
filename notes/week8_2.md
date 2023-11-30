NAT -- Network Address Translation

What
Why
How

Nat machine has to do translation to public facing IP address
What does it know about the packet?

Mac address
Dest IP (example.com)
Src IP (10.x.x.x)
Packet size
Src port (random)
Dest port(80)

Change the Src IP to its own IP address (public facing)

Src IP (example.com)
src port (80)
dest port (NAT box port for this connection)

Orig Dest IP | Orig Port | NAT Port | Orig SRC IP
example.com		xyzw		abcd		10.x.x.x



Choose a new Src port

Example.com thinks its talking to my NAT machine, not to 10.x.x.x