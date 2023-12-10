import sys
import socket
import select
import json

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

def send_server_message(type, words, socket):
    stuff = build_packet(type, words)
    send_data(stuff, socket)

def distribute_message(message, listener, sender, set):
    for s in set:
        if s != sender and s != listener:
            send_server_message("message", message, s)


def decode_message(packet):
    cutpacket = packet[2:] #cut out the length part of packet
    decodedword = cutpacket.decode()
    return decodedword

# def get_next_message(s, buffer_list):
#     #checking to make sure we have a valid word packet
#     if len(buffer_list[s]) >= 2: 
#         encoded_word_length = packet_buffer[:2] 
#         packet_length =  int.from_bytes(encoded_word_length, "big") + 2 #decode passed packet length

#         #check to ensure there is a full word packet in there
#         if len(buffer_list[s]) >= (packet_length):
#             word_packet = packet_buffer[:packet_length]#extract the packet data
#             packet_buffer = packet_buffer[packet_length:]# strip the packet data off the front of the buffer
#             return word_packet


#     pass


def run_server(port):



    read_set = set()

    listen = socket.socket()
    listen.bind(('', port))
    print("Waiting for connections...")
    listen.listen()
    
    read_set.add(listen)

    name_list = {}
    #buffer_list = {}

    # main loop:
    while(True):
        #     call select() and get the sockets that are ready to read
        ready_to_read, _, _ = select.select(read_set, {}, {})


        for s in ready_to_read:
            if s is (listen):
                new_connection, info = s.accept()
                read_set.add(new_connection)
                print(f'{info} connected...')

            else:
                data = s.recv(4096)
                if len(data) == 0:
                    disconnnectedmessage = f'***{name_list[s]} is disconnected...'
                    send_server_message("message", disconnnectedmessage, s)
                    print(connectedmessage)
                    del(name_list[s])
                    read_set.remove(s)

                else:
                    message = decode_message(data)
                    stuff = json.loads(message)
                    if stuff["type"] == "hello":

                        #buffer_list[s] = []
                        name_list[s] = stuff["chat"]
                        connectedmessage = f'***{name_list[s]} is connected...'
                        send_server_message("message", connectedmessage, s)
                        print(connectedmessage)
                        
                    else:
                        print(f'{name_list[s]}: {stuff["chat"]}')
                        distribute_message(stuff["chat"],listen, s, read_set)




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
