

1. application --eg. http, ftp, smtp, imap, send()!
2. transport -- data integrity: TCP, UDP
3. network -- routing, IP (Internet protocol)
4. physical/link -- Ethernet

| <TCP header>|<HTTP header>request data||

#console command:
traceroute -n www.example.com

shows it did like 19 jumps


encapsulation:
TCP vs UDP

tcp: In order, no dups, correctly definitely delivered
UDP: Correct

