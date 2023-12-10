


1.
Starting Nmap 7.80 ( https://nmap.org ) at 2023-12-10 12:39 PST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000093s latency).
All 1000 scanned ports on localhost (127.0.0.1) are closed

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds

2.
Starting Nmap 7.80 ( https://nmap.org ) at 2023-12-10 12:40 PST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000032s latency).
All 65536 scanned ports on localhost (127.0.0.1) are closed

Nmap done: 1 IP address (1 host up) scanned in 1.84 seconds

3.
Starting Nmap 7.80 ( https://nmap.org ) at 2023-12-10 12:42 PST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000030s latency).
Not shown: 65535 closed ports
PORT     STATE SERVICE
3490/tcp open  colubris

Nmap done: 1 IP address (1 host up) scanned in 1.98 seconds


3.b: The server did close, and I suspect its because the portscanner likely sent a rst packet which reset the connection and the server!