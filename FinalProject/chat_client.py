# Example usage:
#
# python select_client.py alice localhost 3490
# python select_client.py bob localhost 3490
# python select_client.py chris localhost 3490
#
# The first argument is a prefix that the server will print to make it
# easier to tell the different clients apart. You can put anything
# there.

import sys
import socket
import time
import random
import threading
import select
import json


from chatui import init_windows, read_command, print_message, end_windows

PACKET_LEN_SIZE = 2

def build_packet(type, words):
    final_packet = b''
    data = {"type": type, "chat": words}
    packet = json.dumps(data)
    packet_bytes = packet.encode()

    packet_len = len(packet)
    packet_len_bytes = packet_len.to_bytes(PACKET_LEN_SIZE, "big")
    
    final_packet += packet_len_bytes + packet_bytes

    return final_packet

def send_data(stuff, socket):
    #string_to_send = stuff
    #string_bytes = string_to_send.encode()
    socket.send(stuff)

def decode_message(packet):
    cutpacket = packet[2:] #cut out the length part of packet
    decodedword = cutpacket.decode()
    return decodedword

#RECV WORK IN PROGRESS
def recieving(socket):
    #how do I do a "ready to read" with only one value?
    read_set = set()
    read_set.add(socket)
    while(True):

        ready_to_read, _, _ = select.select(read_set, {}, {})
        for s in ready_to_read:
            data = s.recv(4096)
            message = decode_message(data)
            stuff = json.loads(message)
            #print(f'{stuff["chat"]}')
            if stuff["name"] == "server":
                print_message(f'{stuff["chat"]}')
            else:
                print_message(f'{stuff["name"]}: {stuff["chat"]}')
            
        



def usage():
    print("usage: select_client.py prefix host port", file=sys.stderr)

def main(argv):
    try:
        name = argv[1]
        host = argv[2]
        port = int(argv[3])
    except:
        usage()
        return 1
    
    init_windows()
    s = socket.socket()
    s.connect((host, port))

    #Can I even do threading in a function like this?
    t1 = threading.Thread(target=recieving, daemon=True,args=(s,))
    t1.start()

    # string_to_send = f"{name}"
    # string_bytes = string_to_send.encode()
    # s.send(string_bytes)

    packet = build_packet("hello", name)
    send_data(packet, s)
    
    while True:
        try:
            command = read_command("Enter a thing> ")
        except:
            break
        print_message(f">>> {command}")
        message_packet = build_packet("message", command)
        send_data(message_packet, s)


    end_windows()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
