
1.
Microsoft IP addresses:
microsoft.com.          0       IN      A       20.112.250.133
microsoft.com.          0       IN      A       20.231.239.246
microsoft.com.          0       IN      A       20.236.44.162
microsoft.com.          0       IN      A       20.70.246.20
microsoft.com.          0       IN      A       20.76.201.171

2.
Google mail server ip addresses:
smtp.google.com.        0       IN      A       172.253.117.27
smtp.google.com.        0       IN      A       74.125.142.26
smtp.google.com.        0       IN      A       74.125.195.27
smtp.google.com.        0       IN      A       74.125.197.26
smtp.google.com.        0       IN      A       172.253.117.26

3. Duckduckgo name servers

duckduckgo.com.         0       IN      NS      dns4.p05.nsone.net.
duckduckgo.com.         0       IN      NS      ns03.quack-dns.com.
duckduckgo.com.         0       IN      NS      dns3.p05.nsone.net.
duckduckgo.com.         0       IN      NS      dns2.p05.nsone.net.
duckduckgo.com.         0       IN      NS      ns01.quack-dns.com.
duckduckgo.com.         0       IN      NS      dns1.p05.nsone.net.
duckduckgo.com.         0       IN      NS      ns02.quack-dns.com.
duckduckgo.com.         0       IN      NS      ns04.quack-dns.com.

4. Dig down to yahoo.com

Dig to find servers:

; <<>> DiG 9.16.1-Ubuntu <<>>
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44190
;; flags: qr rd ra; QUERY: 1, ANSWER: 13, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;.                              IN      NS

;; ANSWER SECTION:
.                       22884   IN      NS      l.root-servers.net.
.                       22884   IN      NS      d.root-servers.net.
.                       22884   IN      NS      k.root-servers.net.
.                       22884   IN      NS      e.root-servers.net.
.                       22884   IN      NS      c.root-servers.net.
.                       22884   IN      NS      b.root-servers.net.
.                       22884   IN      NS      m.root-servers.net.
.                       22884   IN      NS      a.root-servers.net.
.                       22884   IN      NS      h.root-servers.net.
.                       22884   IN      NS      i.root-servers.net.
.                       22884   IN      NS      j.root-servers.net.
.                       22884   IN      NS      g.root-servers.net.
.                       22884   IN      NS      f.root-servers.net.

-------------------------

Choose a server:
dig @l.root-servers.net. www.yahoo.com

; <<>> DiG 9.16.1-Ubuntu <<>> @l.root-servers.net. www.yahoo.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56742
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 13, ADDITIONAL: 27
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.yahoo.com.                 IN      A

;; AUTHORITY SECTION:
com.                    172800  IN      NS      a.gtld-servers.net.
com.                    172800  IN      NS      b.gtld-servers.net.
com.                    172800  IN      NS      c.gtld-servers.net.
com.                    172800  IN      NS      d.gtld-servers.net.
com.                    172800  IN      NS      e.gtld-servers.net.
com.                    172800  IN      NS      f.gtld-servers.net.
com.                    172800  IN      NS      g.gtld-servers.net.
com.                    172800  IN      NS      h.gtld-servers.net.
com.                    172800  IN      NS      i.gtld-servers.net.
com.                    172800  IN      NS      j.gtld-servers.net.
com.                    172800  IN      NS      k.gtld-servers.net.
com.                    172800  IN      NS      l.gtld-servers.net.
com.                    172800  IN      NS      m.gtld-servers.net.

-----------------------------

Choose next server
dig @l.gtld-servers.net. www.yahoo.com

; <<>> DiG 9.16.1-Ubuntu <<>> @l.gtld-servers.net. www.yahoo.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33391
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 5, ADDITIONAL: 10
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.yahoo.com.                 IN      A

;; AUTHORITY SECTION:
yahoo.com.              172800  IN      NS      ns1.yahoo.com.
yahoo.com.              172800  IN      NS      ns5.yahoo.com.
yahoo.com.              172800  IN      NS      ns2.yahoo.com.
yahoo.com.              172800  IN      NS      ns3.yahoo.com.
yahoo.com.              172800  IN      NS      ns4.yahoo.com.


----------------------------------

Reach alias
dig @ns1.yahoo.com. www.yahoo.com

; <<>> DiG 9.16.1-Ubuntu <<>> @ns1.yahoo.com. www.yahoo.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47447
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1272
; COOKIE: 0d2ca9a29e3562a0dae7164f656d68d29e6e267712ef3b5f (good)
;; QUESTION SECTION:
;www.yahoo.com.                 IN      A

;; ANSWER SECTION:
www.yahoo.com.          60      IN      CNAME   me-ycpi-cf-www.g06.yahoodns.net.



-----------------------------------

Repeat with Alias

Dig (same as above)

--------------------------------

Select server:
dig @l.root-servers.net. me-ycpi-cf-www.g06.yahoodns.net.


; <<>> DiG 9.16.1-Ubuntu <<>> @l.root-servers.net. me-ycpi-cf-www.g06.yahoodns.net.
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26489
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 13, ADDITIONAL: 27
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;me-ycpi-cf-www.g06.yahoodns.net. IN    A

;; AUTHORITY SECTION:
net.                    172800  IN      NS      a.gtld-servers.net.
net.                    172800  IN      NS      b.gtld-servers.net.
net.                    172800  IN      NS      c.gtld-servers.net.
net.                    172800  IN      NS      d.gtld-servers.net.
net.                    172800  IN      NS      e.gtld-servers.net.
net.                    172800  IN      NS      f.gtld-servers.net.
net.                    172800  IN      NS      g.gtld-servers.net.
net.                    172800  IN      NS      h.gtld-servers.net.
net.                    172800  IN      NS      i.gtld-servers.net.
net.                    172800  IN      NS      j.gtld-servers.net.
net.                    172800  IN      NS      k.gtld-servers.net.
net.                    172800  IN      NS      l.gtld-servers.net.
net.                    172800  IN      NS      m.gtld-servers.net.

---------------------------------

Select next server
dig @l.gtld-servers.net. me-ycpi-cf-www.g06.yahoodns.net.

; <<>> DiG 9.16.1-Ubuntu <<>> @l.gtld-servers.net. me-ycpi-cf-www.g06.yahoodns.net.
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52828
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 5, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;me-ycpi-cf-www.g06.yahoodns.net. IN    A

;; AUTHORITY SECTION:
yahoodns.net.           172800  IN      NS      ns1.yahoo.com.
yahoodns.net.           172800  IN      NS      ns5.yahoo.com.
yahoodns.net.           172800  IN      NS      ns2.yahoo.com.
yahoodns.net.           172800  IN      NS      ns3.yahoo.com.
yahoodns.net.           172800  IN      NS      ns4.yahoo.com.

-----------------------------------------

Select next server:
dig @ns5.yahoo.com. me-ycpi-cf-www.g06.yahoodns.net.

; <<>> DiG 9.16.1-Ubuntu <<>> @ns5.yahoo.com. me-ycpi-cf-www.g06.yahoodns.net.
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6336
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 4, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1272
; COOKIE: b18bc47c6cf50eff772c952a656d691351541323414a3de2 (good)
;; QUESTION SECTION:
;me-ycpi-cf-www.g06.yahoodns.net. IN    A

;; AUTHORITY SECTION:
g06.yahoodns.net.       172800  IN      NS      yf4.a1.b.yahoo.net.
g06.yahoodns.net.       172800  IN      NS      yf2.a1.b.yahoo.net.
g06.yahoodns.net.       172800  IN      NS      yf1.a1.b.yahoo.net.
g06.yahoodns.net.       172800  IN      NS      yf3.a1.b.yahoo.net.

-----------------------------------------

Reach end:
 dig @yf2.a1.b.yahoo.net. me-ycpi-cf-www.g06.yahoodns.net.


; <<>> DiG 9.16.1-Ubuntu <<>> @yf2.a1.b.yahoo.net. me-ycpi-cf-www.g06.yahoodns.net.
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44018
;; flags: qr aa rd; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;me-ycpi-cf-www.g06.yahoodns.net. IN    A

;; ANSWER SECTION:
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       74.6.160.106
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       69.147.80.15
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       69.147.80.12
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       74.6.160.107