

With UDP and TCP:
-if a packet arrives, it is error free
Uses a checksum to verify correctness

How TCP does it:

ACK packet
window
--Allows senders to sends lots of data without an ACK
(how much data you can send before you get a ack back?)

Allows recievers to exersize _flow control_

_congestion control_ : when the rest of the internet is overloaded

Slow start: start sending out unacknowledged packets and see how much you can get away with

exponential growth

congestion avoidance: send out one more packet each time until that fails

Linear growth