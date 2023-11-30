# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select







def run_server(port):
    # TODO--fill this in


    #VERY VERY UNFINISHED!!!
    # add the listener socket to the set
    #LISTENER SOCKET HERE
    #what is listener socket? s1? data = s1.recv(4098?)
    read_set = set()

    listen = socket.socket()
    listen.bind(('', port))
    print("Waiting for connections...")
    listen.listen()
    
    read_set.add(listen)

    # main loop:
    while(True):
        #     call select() and get the sockets that are ready to read
        ready_to_read, _, _ = select.select(read_set, {}, {})


        #     for all sockets that are ready to read:
        #         if the socket is the listener socket:
        #             accept() a new connection
        #             add the new socket to our set!
        for s in ready_to_read:
            if s is (listen):
                new_connection, info = s.accept()
                read_set.add(new_connection)
                print(f'{info} connected...')
            
        #         else the socket is a regular socket:
        #             recv() the data from the socket
            else:
                data = s.recv(4096)
                if len(data) == 0:
                    print(f'{s.getpeername()} disconected...')
                    read_set.remove(s)
                else:

                    print(f'{s.getpeername()} {len(data)} {data}')
                    #print(data)

                        #if you receive zero bytes
        #                 the client hung up
        #                 remove the socket from tbe set!

    pass

#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
